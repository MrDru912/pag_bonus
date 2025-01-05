#!/bin/bash
#PBS -N one_cpu
#PBS -l select=1:ncpus=64:mem=16gb:scratch_local=10gb
#PBS -l walltime=2:00:00

DATADIR=$HOME/hw01
RESULTDIR=$HOME/experiment_results/$(date +%Y%m%d_%H%M%S)
mkdir -p $RESULTDIR

echo "$PBS_JOBID running on `hostname -f` in $SCRATCHDIR; $PBS_O_WORKDIR" >> $RESULTDIR/job_info.txt
lscpu >> $RESULTDIR/hardware_info.txt

module add cmake
module add gcc
module add openmpi

trap 'clean_scratch' TERM EXIT

test -n "$SCRATCHDIR" || { echo >&2 "SCRATCHDIR not set!"; exit 1; }



# Copy project structure
mkdir -p $SCRATCHDIR/{src,test_data/instances}

cp $PBS_O_WORKDIR/hw01/src/*.cpp $PBS_O_WORKDIR/hw01/src/*.h $SCRATCHDIR/src || { echo >&2 "Error copying source files!"; exit 2; }
cp $PBS_O_WORKDIR/hw01/cmake/CMakeLists.txt $SCRATCHDIR/ || { echo >&2 "Error copying CMakeLists.txt!"; exit 2; }
cp $PBS_O_WORKDIR/hw01/test_data/instances/*.bin $SCRATCHDIR/test_data/instances/ || { echo >&2 "Error copying test data!"; exit 2; }

cd $SCRATCHDIR
mkdir build && cd build
cmake .. || { echo >&2 "CMake failed!"; exit 3; }
make || { echo >&2 "Make failed!"; exit 4; }

mkdir -p results

run_experiment() {
    local threads=$1
    local instance=$2
    local basename=$(basename "$instance")
    local output_file="results/${basename}_t${threads}.txt"
    local time_file="results/${basename}_t${threads}_time.txt"
    local timeout=300

    export OMP_NUM_THREADS=$threads

    echo "Running instance $basename with $threads threads"
    if ! timeout $timeout /usr/bin/time -v ./Storage "../test_data/instances/$basename" "$output_file" 2> "$time_file"; then
            echo "Error: Storage execution failed for $basename with $threads threads" >&2
            echo "Exit code: $?" >&2
    fi

}

threads=(2 4 8 16 32 64)
#instances=(2x5.bin 2x10.bin 5x5.bin) # 5000x20.bin)
instances=($SCRATCHDIR/test_data/instances/*.bin)

for instance in "${instances[@]}"; do
    for t in "${threads[@]}"; do
        run_experiment $t "$instance"
    done
done

cp -r results/* $RESULTDIR/ || { echo >&2 "Failed to copy results!"; exit 5; }
clean_scratch
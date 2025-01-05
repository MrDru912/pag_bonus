import matplotlib.pyplot as plt
import pandas

def plot_performance_graph(problem_sizes, scenarios, max_length_fixed, fixed_param):
    fixed_addition = "max record length" if max_length_fixed else "records number"
    vary_addition = "max record length" if not max_length_fixed else "records number"

    # Plot the graph
    plt.figure(figsize=(10, 6))

    # Plot each scenario
    for scenario_name, execution_times in scenarios.items():
        plt.plot(problem_sizes, execution_times, marker='o', label=scenario_name)

    # Customize the axes (logarithmic for problem size)
    plt.xscale('log')  # Logarithmic scale for X-axis
    plt.xlabel(f'Problem Size (W), {vary_addition}')
    plt.ylabel('Execution Time (T) [s]')

    # Add title, legend, and grid
    plt.title(
        f'Performance Graph: Execution Time vs. Problem Size ({fixed_addition} is fixed: {fixed_param})')
    plt.legend(title='Scenarios', loc='best')
    plt.grid(True)

    # Display the plot
    plt.show()

def create_dict(data):
    scenarios = {
        "CPU Sequential": data[0],
        "2 CPU Parallel": data[1],
        "4 CPU Parallel": data[2],
        "8 CPU Parallel": data[3],
        "16 CPU Parallel": data[4],
        "32 CPU Parallel": data[5],
        "64 CPU Parallel": data[6],
    }
    return scenarios


def get_data(df, instances):
    data = []
    for i in [1,2,4,8,16,32,64]:
        arr = []
        for j in instances:
            time = df[f'time,ms (p={i})'][j-1]
            arr.append(None if time == 'timeout' else int(time))
        data.append(arr)
    return data
df = pandas.read_csv('pag_bonus.csv')

# max length fixed
problem_sizes = [10, 100, 1000, 10000]
scenarios = create_dict(get_data(df, [1,4,7,10]))
plot_performance_graph(problem_sizes, scenarios, True, 10)

new_scenarios = create_dict(get_data(df, [2,5,8,11]))
print(new_scenarios)
plot_performance_graph(problem_sizes, new_scenarios, True, 100)

new_scenarios = create_dict(get_data(df, [3,6,9,12]))
plot_performance_graph(problem_sizes, new_scenarios, True, 1000)


# records number fixed
problem_sizes = [10, 100, 1000]
scenarios = create_dict(get_data(df, [1,2,3]))
plot_performance_graph(problem_sizes, scenarios, False, 10)

new_scenarios = create_dict(get_data(df, [4,5,6]))
plot_performance_graph(problem_sizes, new_scenarios, False, 100)

new_scenarios = create_dict(get_data(df, [7,8,9]))
plot_performance_graph(problem_sizes, new_scenarios, False, 1000)

new_scenarios = create_dict(get_data(df, [10,11,12]))
print(new_scenarios)
plot_performance_graph(problem_sizes, new_scenarios, False, 10000)

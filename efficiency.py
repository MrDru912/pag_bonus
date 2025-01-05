import matplotlib.pyplot as plt
import pandas


def plot_efficiency_graph(problem_sizes, efficiencies, max_length_fixed, fixed_param):
    fixed_addition = "max record length" if max_length_fixed else "records number"
    vary_addition = "max record length" if not max_length_fixed else "records number"

    plt.figure(figsize=(10, 6))

    for threads, efficiency in efficiencies.items():
        plt.plot(problem_sizes, efficiency, marker='o', label=f'{threads} Threads')

    plt.xscale('log')  # Logarithmic scale for X-axis
    plt.xlabel(f'Problem Size (W), {vary_addition}')
    plt.ylabel('Efficiency (E)')

    plt.title(f'Efficiency Graph: Efficiency vs. Problem Size ({fixed_addition} is fixed: {fixed_param})')
    plt.legend(title='Number of Threads (p)', loc='lower right')
    plt.grid(True)

    plt.show()

def create_dict(data):
    scenarios = {
        2: data[0],
        4: data[1],
        8: data[2],
        16: data[3],
        32: data[4],
        64: data[5],
    }
    return scenarios


def get_data(df, instances):
    data = []
    for i in [2,4,8,16,32,64]:
        arr = []
        for j in instances:
            time = df[f'efficiency(p={i})'][j-1]
            arr.append(None if time == '#VALUE!' else float(time.replace(',', '.')))
        data.append(arr)
    return data

df = pandas.read_csv('pag_bonus.csv')

# max length fixed
problem_sizes = [10, 100, 1000, 10000]
efficiencies = create_dict(get_data(df, [1,4,7,10]))
print(efficiencies)
plot_efficiency_graph(problem_sizes, efficiencies, True, 10)

efficiencies = create_dict(get_data(df, [2,5,8,11]))
print(efficiencies)
plot_efficiency_graph(problem_sizes, efficiencies, True, 100)

efficiencies = create_dict(get_data(df, [3,6,9,12]))
print(efficiencies)
plot_efficiency_graph(problem_sizes, efficiencies, True, 100)

# records number fixed
problem_sizes = [10, 100, 1000]
efficiencies = create_dict(get_data(df, [1,2,3]))
plot_efficiency_graph(problem_sizes, efficiencies, False, 10)

efficiencies = create_dict(get_data(df, [4,5,6]))
plot_efficiency_graph(problem_sizes, efficiencies, False, 100)

efficiencies = create_dict(get_data(df, [7,8,9]))
plot_efficiency_graph(problem_sizes, efficiencies, False, 1000)

efficiencies = create_dict(get_data(df, [10,11,12]))
print(efficiencies)
plot_efficiency_graph(problem_sizes, efficiencies, False, 10000)

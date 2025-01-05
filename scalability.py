import matplotlib.pyplot as plt


def plot_performance_graph(speedups, max_length_fixed, fixed_param):
    # Data for threads, speedup, and problem sizes
    threads = [2, 4, 8, 16, 32, 64]

    # Plot the graph
    plt.figure(figsize=(10, 6))

    for size, speedup in speedups.items():
        plt.plot(threads, speedup, marker='o', label=f'N = {size}')

    # Adding titles and labels
    plt.title('Scalability Graph: Speedup vs. Number of Threads')
    plt.xlabel('Number of Threads (p)')
    plt.ylabel('Speedup (S)')
    plt.grid(True)
    fixed_str = "max record length" if max_length_fixed else "records number"
    vary_str = "records number" if max_length_fixed else "max record length"
    plt.legend(title=f'Problem Size (N is {vary_str},\n{fixed_str} is fixed: {fixed_param})', loc='best')
    plt.xticks(threads)

    # Show the plot
    plt.show()


# fixed max length
speedups = {
    10: [1, 1, 1, 1, 0.5, 0.04166666667],
    100: [2.034482759,	2.034482759, 1.035714286, 0.935483871, 0.875, 0.8857142857],
    1000: [1.758208955, 3.365714286, 3.526315789, 3.181818182, 2.714285714, 0.7638888889],
    10000: [1.815271407,3.556894077,3.843290891,3.784786204,3.535930736,3.304449649],
}
plot_performance_graph(speedups, True, 10)

speedups = {
    10: [1,2,1,0.3333333333,0.6666666667,0.1875],
    100: [1.785185185, 3.442857143, 3.461538462, 3.043478261, 2.294117647, 0.6216216216],
    1000: [1.818699608, 3.631221385, 3.968007044, 3.971260997, 3.952436195, 3.666666667],
    10000: [None, None, None, None, None, 4.722301546],
}
plot_performance_graph(speedups, True, 100)

speedups = {
    10: [2.034482759, 2.034482759, 1.035714286, 0.935483871, 0.875, 0.8857142857],
    100: [1.818027572, 3.637598133, 3.945606695, 3.872637634, 3.324061196, 1.67862069],
    1000: [None, None, None, None, 3.988344077, 1.997215095],
    10000: [None, None, None, None, None, None],
}
plot_performance_graph(speedups, True, 1000)


# fixed records number
speedups = {
    10: [1, 1, 1, 1, 0.5, 0.04166666667],
    100: [1, 2, 1, 0.3333333333, 0.6666666667, 0.1875],
    1000: [2.034482759, 2.034482759, 1.035714286, 0.935483871, 0.875, 0.8857142857],
}
plot_performance_graph(speedups, False, 10)

speedups = {
    10: [1, 1.666666667, 2.5, 1.5, 0.5, 0.08333333333],
    100: [1.785185185, 3.442857143, 3.461538462, 3.043478261, 2.294117647, 0.6216216216],
    1000: [1.818027572, 3.637598133, 3.945606695, 3.872637634, 3.324061196, 1.67862069],
}
plot_performance_graph(speedups, False, 100)

speedups = {
    10: [1.758208955, 3.365714286, 3.526315789, 3.181818182, 2.714285714, 0.7638888889],
    100: [1.818699608, 3.631221385, 3.968007044, 3.971260997, 3.952436195, 3.666666667],
    1000: [None, None, None, None, 3.988344077, 1.997215095],
}
plot_performance_graph(speedups, False, 1000)

speedups = {
    10: [1.815271407, 3.556894077, 3.843290891, 3.784786204, 3.535930736, 3.304449649],
    100: [None, None, None, None, None, 4.722301546],
    1000: [None, None, None, None, None, None],
}
plot_performance_graph(speedups, False, 10000)




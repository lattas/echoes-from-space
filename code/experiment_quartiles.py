"""
Creates quartiles from experiment data.

Quartiles: https://goo.gl/mXrKM8
Visualize: https://goo.gl/hXmSuK
"""

import matplotlib.pyplot as plt
from experiment_data import amateur_times, expert_times


def display_quartiles():
    """
    Boxplots the experiment data
    :return: 
    """
    # plt.boxplot(expert_times[0], showmeans=True)
    # plt.boxplot(expert_times[1], showmeans=True)
    # plt.boxplot(amateur_times[0], showmeans=True)
    # plt.boxplot(amateur_times[1], showmeans=True)

    times = [amateur_times[0], expert_times[0], amateur_times[1], expert_times[1]]

    legend = plt.legend(loc='upper right')
    box = plt.boxplot(times, 0, sym='', showmeans=False, whis=99,
                      labels=['Amateurs, Different', 'Experts Different',
                              'Amateurs Same', 'Experts Same'])

    plt.ylim([0, 40])
    plt.grid(True, axis='y')
    plt.ylabel("Time (seconds) to click on command")
    plt.xticks([1, 2, 3, 4], ['Amateurs,\nDifferent',
                              'Experts,\nDifferent',
                              'Amateurs,\nSame',
                              'Experts,\nSame'])

    plt.savefig('experiment-boxplot.eps')
    plt.show()


def basic_stats(data):
    """
    Returns min, median, mean, max
    :param data: experiment data
    :return: min, median, mean, max as formatted string
    """
    # min = str(data[])
    print(data)


# Run
display_quartiles()
basic_stats(expert_times)

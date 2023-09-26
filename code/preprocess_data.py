"""
Organizes experiment data.

Usage: python experiment_data.py stats_file.py
"""

import numpy as np
import sys
import datetime
from random import shuffle

EXPERIMENT_STATS_FILE = sys.argv[1]

AMATEURS = ["2017-06-18_20-46",
            "2017-06-19_11-42",
            "2017-06-19_12-07",
            "2017-06-19_12-18",
            "2017-06-19_12-46",
            "2017-06-19_13-04",
            "2017-06-19_13-45"]

EXPERTS = ["2017-06-19_18-02",
           "2017-06-19_18-12",
           "2017-06-19_18-20",
           "2017-06-19_19-30"]


def cleanse(filename):
    """
    Cleans and outputs the given experiment data as a list
    :param filename:
    return cleansed data
    """

    moves = []

    with open(filename) as test_input:
        for line in test_input:
            move = line.split("\n")[0]
            moves.append([
                float(move.split(" ")[0]),  # Time
                move.split(" ")[1].split("_")[0]  # Action Type
            ])

    return moves


def count_time(moves):
    """
    Counts times between moves and their type
    :param moves: 
    :return: 
    """

    action_times = []
    starting_time = float(moves.pop(0)[0])

    command_type = 0  # type 0 means the action involved changing the en
                      # type 1 means the action remained in the same en

    for move in moves:
        if move[1] == "vm":

            action_times.append([
                move[0] - starting_time,  # time taken to since last command
                command_type                      # type of command
            ])

            starting_time = move[0]
            command_type = 1
        else:
            command_type = 0

    return action_times

amateur_times = [[], []]
expert_times = [[], []]


def input_all():
    """
    Aggregates all experiment input
    :return: 
    """

    for filename in AMATEURS:
        for move in count_time(cleanse(
                        "../data/results/" + filename)):
            amateur_times[move[1]].append(move[0])
    for filename in EXPERTS:
        for move in count_time(cleanse(
                        "../data/results/" + filename)):
            expert_times[move[1]].append(move[0])

    
def get_stats(data):
    """
    returns basic statistics for the input data
    :param data: 
    :return: 
    """
    
    min = "min: " + str(np.min(data))
    max = ", max: " + str(np.max(data))
    median = ", median: " + str(np.median(data))
    mean = "mean: " + str(np.mean(data))

    return min + max + median + mean + "\n"


def all_stats():
    """
    returns all general stats for the experiment data
    :return: 
    """

    with open(EXPERIMENT_STATS_FILE, "w") as f:

        f.write(str(datetime.date.today()))  # date

        f.write("\n" + str(len(AMATEURS)) + " amateur tests and "
                + str(len(EXPERTS)) + " expert tests.")  # exp data

        f.write("\nAmateurs changing entities:\n" + get_stats(amateur_times[0]))
        f.write("\nAmateurs not changing entities\n" + get_stats(amateur_times[1]))
        f.write("\nExperts changing entities:\n" + get_stats(expert_times[0]))
        f.write("\nExperts not changing entities\n" + get_stats(expert_times[1]))

        f.write("\nExperts were " + str(
            np.mean(amateur_times[0] + amateur_times[1])
            / np.mean(expert_times[0] + expert_times[1])
        ) + " times faster.")


# Run
input_all()
all_stats()
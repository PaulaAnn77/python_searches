#  Paula Farebrother
#  Created: July 2024
# Last modified: oct 2024
# ______________________________________________________
import random


def linear_search_steps(runs, elements):
    """ Creates a list of elements with length as arg and iterates for a given
        number of runs.
        List is shuffled and each item is checked in list and returned to a list
        if not matched, or confirmed as a match.
    """
    test_data = [y + 1 for y in range(elements)]
    steps_list = []
    steps_count = 0
    average_total = []

    for i in range(0, runs):
        random.shuffle(test_data)
        num = random.random()
        target = int(num * (len(test_data) * 2))
        print()
        print("Looking for target number: {}".format(target))
        for t in test_data:
            if t == target:
                steps_count += 1
                steps_list.append(steps_count)
                print("Match found in {} steps". format(steps_count))
                break
            elif t != target:
                steps_count += 1
                steps_list.append(steps_count)
                if steps_count == len(test_data):
                    print("No match was found in this list of {} "
                          "elements.".format(steps_count))

        if len(steps_list) < elements:
            average_total.append(average_steps(steps_list))
        elif len(steps_list) == elements:
            print("No matches found")
        steps_list = []
        steps_count = 0
    print()
    print("Overall total average is:")
    average_steps(average_total)


def average_steps(steps_list):
    """ calculates and returns average number of steps taken during search """
    length = len(steps_list)
    total = sum(steps_list)
    average = round(total / length)
    print("Average steps:", average)
    return average

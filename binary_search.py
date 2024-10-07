#  Paula Farebrother
#  Created: July 2024
#  Last modified: Oct 2024

comp_list = []

def binary_search_iterative(ordered_list, term):
    """ Checks if a list is ordered and has duplicates
        uses binary search algorithm to search for a term
        returns number of comparisons to a global variable to compare averages
    """
    global comp_list
    size_of_list = len(ordered_list) - 1
    index_of_first_element = 0
    index_of_last_element = size_of_list
    comparisons = 0

    if is_sorted(ordered_list):
        if has_duplicates(ordered_list) is False:
            while index_of_first_element <= index_of_last_element:
                mid_point = (index_of_first_element + index_of_last_element) // 2
                comparisons += 1
                if ordered_list[mid_point] == term:
                    print("Target found in {} comparisons".format(comparisons))
                    comp_list.append(comparisons)
                    return mid_point
                if term > ordered_list[mid_point]:
                    index_of_first_element = mid_point + 1
                else:
                    index_of_last_element = mid_point - 1
            if index_of_first_element > index_of_last_element:
                print("Target not found")
                return None
        if has_duplicates(ordered_list):
            print("This list has duplicates")
    else:
        print("List must be sorted first.")


def is_sorted(list):
    """ checks each item in a list to ensure it is sorted in ascending order
    """
    for i in range(len(list) - 1):
        if list[i] > list[i+1]:
            return False  # List is not sorted
    return True  # List is sorted


def has_duplicates(list):
    """ Checks all items across the list for duplicates.
        Returns True if duplicates exist
        Returns False if no duplicates exist
    """
    new_list = []  # set a blank list to hold each list element once checked
    for i in list:
        if i in new_list:
            return True  # has duplicates
        new_list.append(i)
    return False  # doesn't have duplicates


def average_steps(comp_list):
    """ calculates and returns average number of steps taken during search """
    length = len(comp_list)
    total = sum(comp_list)
    average = round(total / length)
    print("Average steps:", average)
    return average

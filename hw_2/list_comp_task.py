import statistics
from collections import Counter


# Total amount of received integers.
def total_amount(test_list):
    return len(test_list)


# Total amount of different values the array has.
def unique_amount(test_list):
    return len(set(test_list))


# Total amount of values that occur only once.
def once_occure_amount(test_list):
    result = [x for x in test_list if test_list.count(x) == 1]
    return len(result)


# (4) It is (or they are) the element(s) that has (or have) the maximum occurrence.
# If there are more than one, the elements should be sorted (by their value obviously)
def max_occurance_elements(test_list):
    result = statistics.multimode(test_list)
    return sorted(result)


# (5) Maximum occurrence of the integer(s)
def max_occurance(test_list):
    count_num_occurrence = Counter(test_list)
    max_occurrence = max(count_num_occurrence.values())
    max_count_of_integer = [count for num, count in count_num_occurrence.items() if count == max_occurrence]
    return max_count_of_integer


# Make the list from (4) and (5) tasks:
def make_list_4_and_5(test_list):
    return [max_occurance_elements(test_list), max_occurance(test_list)]


def stat(test_list):
    final_list = [total_amount(test_list),
                  unique_amount(test_list),
                  once_occure_amount(test_list)
                  ]
    final_list.extend([make_list_4_and_5(test_list)])
    return final_list

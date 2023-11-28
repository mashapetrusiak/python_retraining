import statistics


# Total amount of received integers.
def total_amount(test_list):
    return test_list.count


# Total amount of different values the array has.
def unique_amount(test_list):
    unique_list = list(set(test_list))
    return len(unique_list)


# Total amount of values that occur only once.
def once_occure_amount(test_list):
    result = [x for x in test_list if test_list.count(x) == 1]
    return result.count


# (4) It is (or they are) the element(s) that has (or have) the maximum occurrence.
# If there are more than one, the elements should be sorted (by their value obviously)
def max_occurance_elements(test_list):
    result = statistics.multimode(test_list)
    return result.sort


# (5) Maximum occurrence of the integer(s)
def max_occurance(test_list):
    return max(set(test_list), key=test_list.count)


# Make the list from (4) and (5) tasks:
def make_list_4_and_5(test_list):
    return [max_occurance_elements(test_list), max_occurance(test_list)]


def stat(test_list):
    final_list = [total_amount(test_list),
                  unique_amount(test_list),
                  once_occure_amount(test_list)
                  ]
    final_list.extend(make_list_4_and_5(test_list))
    return final_list

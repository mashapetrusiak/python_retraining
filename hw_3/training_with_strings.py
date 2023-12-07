# Cut the string into chunks (a chunk here is a substring of the initial string) of size n
def splited_string(input_data, n):
    if n <= 0 or n > len(input_data):
        return ""
    else:
        result = [input_data[i:i + n] for i in range(0, len(input_data), n)]
        return result


# Ignore the last chunk if its size is less than n
def filtered_result(input_data, n):
    splited_str = splited_string(input_data, n)

    if len(splited_str) == 0:
        return splited_str
    elif len(splited_str[-1]) < n:
        splited_str.pop(-1)
        return splited_str
    else:
        return splited_str


# Check the sum of the cubes of its digits is divisible by 2
def check_sum_of_cube(num):
    sum_el = 0
    for i in num:
        sum_el += int(i) ** 3
    return sum_el % 2 == 0


# Rotation string to the left by one position
def rotate(strg, n):
    res = strg[n:] + strg[0]
    return(res)


# If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2,
# reverse that chunk; otherwise rotate it to the left by one position.
def converting_of_elements(input_data, n):
    splited_str = filtered_result(input_data, n)
    final_result = []
    for el in splited_str:
        if check_sum_of_cube(el):
            el = el[::-1]
        else:
            el = rotate(el, 1)
        final_result.append(el)
    return ''.join(final_result)

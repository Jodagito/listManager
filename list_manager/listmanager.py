def subtract_elements(array):
    return list(map(lambda x, y: x - y, array, array[1:]))


def multiply_elements(array):
    return list(map(lambda x, y: x * y, array, array[1:]))


def divide_elements(array):
    return list(map(lambda x, y: x / y, [x for x in array if x != 0],
                    [y for y in array[1:] if y != 0]))


def remove_repeated_elements(array):
    new_array = [x for x in array if array.count(x) == 1]
    return new_array


def return_common_elements(array0, array1):
    return list(filter(lambda x: x in array1, array0))


def return_uncommon_elements(array0, array1):
    return list(filter(lambda x: x not in array1, array0))


def return_element_index(array, element):
    return [x[0] for x in enumerate(array) if x[1] == element]


def element_average(array, element):
    return array.count(element) / len(array) * 100


def array_average(array):
    from functools import reduce
    return reduce(lambda x, y: x + y, array) / len(array)


def array_mode(array):
    return max([array.count(x) for x in array])


def odd_array_median(array):
    return list(filter(lambda x: len(array) % 2 == 1 and
                       x == array[len(array) // 2], array))[0]


def pair_array_median(array):
    return (array[::1][len(array) // 2 - 1] + array[len(array) // 2]) / 2

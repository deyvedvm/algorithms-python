"""
The optimal solution (Kadane's algorithm) for the maximum sum subarray problem and how to arrive at it by optimizing
less efficient algorithms.
"""


def three_loops(array):
    n = len(array)
    max_sum = array[0]
    for start in range(n):
        for end in range(start, n):
            current_sum = sum(array[start: end + 1])
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


def two_loops(array):
    n = len(array)
    max_sum = array[0]
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += array[end]  # update the current sum as we go
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum


def one_loop(array):
    n = len(array)
    max_sum = array[0]
    current_sum = array[0]
    for i in range(1, n):
        current_sum = max(current_sum + array[i], array[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


first_array = [3, 4, -9, 1, 2]
second_array = [1, 2, 3]
third_array = [-1, -2, -3]

assert three_loops(first_array) == two_loops(first_array)
assert three_loops(second_array) == two_loops(second_array)
assert three_loops(third_array) == two_loops(third_array)

assert one_loop(first_array) == two_loops(first_array)
assert one_loop(second_array) == two_loops(second_array)
assert one_loop(third_array) == two_loops(third_array)

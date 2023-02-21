#I Write a function that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals only be counted once.

#Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value.
#Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

#List containing overlapping intervals:
#[
#   [1, 4],
#   [7, 10],
#   [3, 5]
#]

#Examples

# sumIntervals( [
#    [1, 2],
#    [6, 10],
#    [11, 15]
# ] )
# result is 9

# sumIntervals( [
#    [1, 5],
#    [10, 20],
#    [1, 6],
#    [16, 19],
#    [5, 11]
# ] )
# result is 19


def sum_of_intervals(intervals):
    count_of_digit = []
    for first_digit, second_digit in intervals:
        for counter in range(first_digit+1, second_digit+1):
            count_of_digit.append(counter)
    return len(set(count_of_digit))

# 4 kyu sum of intervals kata
# i writed a program that accepts an array of intervals, and returns the sum of all the intervail lengths. 


def sum_of_intervals(intervals):
    count = []
    for min, max in intervals:
        for j in range(min+1, max+1):
            count.append(j)
    return len(set(count))

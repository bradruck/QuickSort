# Quick Sort Run-Times, Assignment #7 - P12.9
# Programmer: Bradley Ruck
# CSC 217 470
# Date Created: 7/22/2016
# Date of Final Update: 7/24/2016

# Two Quicksort algorithms that measure the difference between sorting with a single pivot point (two
# partitions) and three partitions.  The difference in speed becomes particularly evident when the list
# has a larger number of repeated elements. The output highlights the ten-fold increase in speed achieved
# via the utilization of an additional partition.
#
# Variables/Definitions used:   quickSort2 - function that returns an ascending sorted list via 2 partitions
#                               partition - function that returns the pivot point to quickSort2
#                               quickSort3 - function that returns an ascending sorted list via 3 partitions
#                               swap - function that returns two list values that have had their positions switched
#                               pivot - element values that determines the positions of the partition splits
#                               values_2way, values_3way - lists of elements to be sorted
#                               minPos - position of the minimum element in the list
#                               n - user provided data for sort size
#                               x - user provided data for determining maximum element variety
#                               startTime(1)(2), endTime(1)(2) - starting and ending times of the sorts
#

from random import randint
from time import time

# Function to sort recursively with 2 Partitions
#
def quickSort2(values, start, to) :
    if start >= to :
        return
    p = partition(values, start, to)
    quickSort2(values, start, p)
    quickSort2(values, p + 1, to)

# Function to find a single pivot point in a list
#
def partition(values, start, to) :
    pivot = values[start]
    i = start - 1
    j = to + 1
    while i < j :
        i += 1
        while values[i] < pivot :
            i += 1
        j -= 1
        while values[j] > pivot :
            j -= 1
        if i < j :
            swap(values, i, j)
    return j

# Function to sort recursively with 3 Partitions
#
def quickSort3(values, start, to) :
    if start >= to : return
    pivot = values[start]
    e = i = start
    g = to
    while i <= to :
        if values[i] < pivot :
            swap(values, i, e)
            e += 1
            i += 1
        elif values[i] == pivot :
            i += 1
        else :
            to -= 1
            swap(values, i, g)
    quickSort3(values, start, e)
    quickSort3(values, g, to)

# Function to swap the value of 2 element locations in a list
#
def swap(values, i, j) :
    temp = values[i]
    values[i] = values[j]
    values[j] = temp

# Main driver function to create list, run sort and print the computational times for comparision
#
def main() :
    # Prompt for the sort size and maximum element variety
    print()
    n = int(input("Enter the list size: "))
    print()
    print("Enter the maximum element number from which to build the list (the minimum is set at 1)")
    x = int(input("(Hint, the lower the number, the higher number of duplicate elements with which to prove the algorithm's speed): "))

    # Construct the random list to sort
    #
    values_2way = []
    for i in range(n) :
        values_2way.append(randint(1, x))
    values_3way = values_2way       # Create a duplicate list to assure apples to apples comparision

    # Get the time at the start of the sort, sort, then get the time at the end of the sort
    #
    startTime2 = time()
    quickSort2(values_2way, 0, n - 1)
    endTime2 = time()

    print()
    print("The number of seconds for the 2-way sort was:  %.8f" % (endTime2 - startTime2))

    # Get the time at the start of the sort, sort, then get the time at the end of the sort
    #
    startTime3 = time()
    quickSort3(values_3way, 0, n - 1)
    endTime3 = time()

    print()
    print("The number of seconds for the 3-way sort was:  %.8f" % (endTime3 - startTime3))

    print()
#    print(values_2way)
#    print(values_3way)

# Run the program
#
main()

#!/usr/bin/env python3
#These are my comprehensive notes for my Data Structures and Algorithms course.
import math as m
def assignment_one_notes():
    '''
    Assignment One Notes::
    # Complexity Analysis:
        - The ability to predict the time and space complexity of an algorithm
        - T(n) = the number of operations executed in worst case for processing input of size n
        - To determine this, count the number of basic operations in the algorithm, Ex:
            - addition = 1 operation
            - calling a method or returning from a method = 1 operation
            - index in an array = 1 operation
            - comparison = 1 operation
        - remove multipliers and non-dominant terms

        - if we have 3log(n) + log(log(n)), its complexity is O(log(n)), so log(n) grows faster than log(log(n)).

        - Relatives of Big-Oh::
            - Big-Omega (Ω): lower bound (Best case)
            - Big-Theta (Θ): tight bound (Average case)
            - Big-O (O): obviously upper bound (Worst case)
            - Little-o (o): strict upper bound (not a tight bound) - Basically, Little-o cannot share the same growth rate as the function it is bounding.
            - Little-omega (ω): strict lower bound (not a tight bound) - Bsically, the same but for a lower bound.

        - Divide and Conquer Algorithms:
            - Divide: break the problem into subproblems
            - Conquer: solve the subproblems recursively
            - Combine: combine the solutions of the subproblems to solve the original problem
            - To find the complexity of a DAC Algorithm, you must use a Recurrence Relation
                - 3 Main methods: Substitution, Recursion Tree, and the main one, the Master Theorem
                - For sake of time, I'm only going to be studying the Master Theorem for the Final
                    - Master Theorem:
                        Let a>=1 and b>1 be const, let f(n) be a function, and let T(n) be defined on +/0 ints by recurrence:
                            T(n) = aT(n/b) + f(n) || Here n/b is either floor or ceiling of n/b, then T can have the following bounds:
                                if f(n) = O(n^log_ba - ε) for some ε>0, then T(n) = Θ(n^log_ba)
                                if f(n) = Θ(n^log_ba), then T(n) = Θ(n^log_ba * log n)
                                if f(n) = Ω(n^log_ba + ε) for some ε>0, and if af(n/b) <= cf(n) for some c<1 and sufficiently large n, then T(n) = Θ(f(n))
                                - All of this is a fancy way to say: COMPARE A AND B^D where f(n) = Θ(n^d)
                                    - if a < b^d, then T(n) = Θ(n^d)
                                    - if a = b^d, then T(n) = Θ(n^d log n)
                                    - if a > b^d, then T(n) = Θ(n^log_ba)
                                - We are checking to see whether the recursive part or the non-recursive part of an algorithm is heavier.
    '''
    return None

def assignment_two_notes():
    '''
    Assignment Two Notes::
    - Maximum-Subsequence Problem:
        - given an array of numbers, find the contiguous subarray with the largest sum.
    '''
    return None

def assignment_three_notes():
    '''
    Assignment Three Notes::
        Sorting Algorithms:
            - Basic Sorting Algorithms: Bubble Sort, Insertion Sort, Selection Sort
            - Advanced Sorting Algorithms: Shell Sort, Heap Sort, Quick Sort, Merge Sort, Counting Sort, Radix Sort, Bucket Sort
            - Inversions:
                - An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j]
                - An array with few inversions is almost sorted, an array with many is far from sorted
                - Maximum number of inversions in an array of size n is n(n-1)/2, average number of inversions is n(n-1)/4
            - Sensitive Algorithms: these perform differently based on how sorted the array is, AKA, how many inversions the array has.
                - Examples: Insertion Sort, Bubble Sort
            - Important Note: ANY algorithm that sorts by exchanging adjacent elements REQUIRES theta(n^2) time to exeute
            - ALSO: ANY algorithm that compares elements REQUIRES theta(n log n) time to execute
            - INSERTION SORT::
                - Array is divided into sorted and unsorted parts, and elements from the unsorted part are picked out and placed correctly into the sorted part.
                - Best case: O(n) time (when array is already sorted)
                - Average case: O(n^2) time
                - Worst case: O(n^2) time (when array is sorted in reverse order)
                - Summary: VERY simple, but highly inefficient on even moderately large lists. VERY sensitive
            - BUBBLE SORT::
                - Compares adjacent elements, swapping them if needed, then moves to the next pair, ad infinitum until end of array.
                - Very easy to reverse sort
                - Best case: O(n) time (when array is already sorted)
                - Average case: O(n^2) time
                - Worst case: O(n^2) time (when array is sorted in reverse order)
                - Summary: Simple, but highly inefficient on even moderately large lists. Not very sensitive if using basic version as it always runs n^2 time if list isn't sorted.
            - SELECTION SORT::
                - Divides array, like past 2, but casts find min or find max and shoves them to the right part of the array.
                - Best case: O(n^2) time
                - Average case: O(n^2) time
                - Worst case: O(n^2) time
                - Summary: Simple, but highly inefficient on even moderately large lists. Not sensitive at all
            - SHELL SORT::
                - An optimization of Insertion Sort that allows the exchange of items that are far apart.
                - It compares non-consevutive elements 
    '''
    return None

#Assignment One Code Examples::
def binary_search (arr, start, end, key):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return None
def binary_search_recursive(arr, start, end, key):
    if start > end:
        return None
    mid = start + (end - start) // 2
    if arr[mid] < key:
        return binary_search_recursive(arr, mid + 1, end, key)
    elif arr[mid] > key:
        return binary_search_recursive(arr, start, mid - 1, key)
    else:
        return mid
#End Assingment One Code Examples

#Assignment Three Code Examples::
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        print(arr)
        arr[j+1] = key
    return arr
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
        print(arr)
    return arr
def selection_sort(arr):
    n = len(arr)
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j    
        print(arr)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
#End Assignment Three Code Examples

def main():# Examples with code go here!
    
    print("\nAssignment One Examples::")
    #Binary Search Example (with an already sorted array as input)
    arr = [2, 3, 4, 10, 40]
    arr2 = [1, 5, 8, 12, 20, 25, 30]
    key = 10
    key2 = 20
    result = binary_search(arr, 0, len(arr)-1, key)
    result_recursive = binary_search_recursive(arr2, 0, len(arr)-1, key2)
    print("Non-Recursive Array and Key: ", arr, key, "\n", "Non-Recursive Results: ", result)
    print("Recursive Array and Key: ", arr2, key2,  "\n", "Recursive Results: ", result_recursive)
    print("End of Assignment One Examples\n")

    print("Assignment Three Examples::")
    arr_ins = [12, 500, 3, 4, 6, -10]
    sorted_arr_ins = insertion_sort(arr_ins)
    print("Insertion Sort Result: ", sorted_arr_ins)
    arr_bub = [64, 34, -5, 25, 12, 22, 11, -5, 90, -10]
    sorted_arr_bub = bubble_sort(arr_bub)
    print("Bubble Sort Result: ", sorted_arr_bub)
    arr_sel = [29, 10, 14, -500, 37, 13, -10]
    sorted_arr_sel = selection_sort(arr_sel)
    print("Selection Sort Result: ", sorted_arr_sel)
    print("End of Assignment Three Examples\n")


    #print("Assignment Four Examples::")
    #print("End of Assignment Four Examples\n")    


    #print("Assignment Five Examples::")
    #print("End of Assignment Five Examples\n")


    #print("Assignment Six Examples::")
    #print("End of Assignment Six Examples\n")


    #print("Assignment Seven Examples::")
    #print("End of Assignment Seven Examples\n")



if __name__ == "__main__":
    main()
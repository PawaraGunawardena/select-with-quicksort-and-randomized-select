import random
import time

def quicksort(A, p, r):

    if(p < r):
        q = partition(A, p,r)
        quicksort(A, p, q-1)
        quicksort(A, q+1,r)

def partition(A,p,r):
    x = A[r]
    i = p-1
    j = p
    while j < r:
        if A[j] <= x:
            i = i+1
            k = A[j]
            A[j] = A[i]
            A[i] = k
        j = j+1
    h = A[i+1]
    A[i+1] = A[r]
    A[r] = h
    return i+1

def sort_by_quicksort(input_array, random_select_list_indices):
    r = len(input_array) - 1
    p = 0
    time_selection_after_sorting=0
    time_gap=0

    for select_index in random_select_list_indices:

        start_time = time.time()
        quicksort(input_array, p, r)
        x = input_array[select_index]
        end_time = time.time()
        # print(x)
        random.shuffle(input_array)

        time_gap = end_time-start_time
        time_selection_after_sorting+=time_gap
    quicksort(input_array, p, r)
    print(input_array)
    return (time_selection_after_sorting)

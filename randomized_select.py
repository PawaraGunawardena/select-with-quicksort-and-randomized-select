import random
import time

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

def randomized_partition(A,p,r):
    q = random.randint(p,r)
    k = A[q]
    A[q] = A[r]
    A[r] = k
    return partition(A,p,r)

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]

    q = randomized_partition(A, p, r)
    k = q - p + 1

    if i == k:
        return A[q]
    else:
        if i < k:
            return randomized_select(A, p, q - 1, i)
        else:
            return randomized_select(A, q + 1, r, i - k)

def select_by_randomizedselect(input_array, random_select_list_indices):
    r = len(input_array) - 1
    p = 0
    time_selection_after_sorting=0
    time_gap=0

    for select_index in random_select_list_indices:

        start_time = time.time()
        x=randomized_select(input_array, p, r, select_index+1)
        end_time = time.time()
        # print(x)
        random.shuffle(input_array)

        time_gap = end_time-start_time
        time_selection_after_sorting+=time_gap

    return (time_selection_after_sorting)

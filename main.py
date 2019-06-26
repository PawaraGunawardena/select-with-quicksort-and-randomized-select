import random
import sys
import randomized_select
import quicksort

no_of_selections = 1000
input_array_length =1000000
input_array = []

def generate_item_list():
    while True:
        temp = random.randint(0,sys.maxsize)
        if(temp not in input_array):
            input_array.append(temp)
        if(len(input_array) == input_array_length):
            break;

    return (input_array)

def random_select_list():
    index_range = int(input_array_length/no_of_selections)
    start_range = 0
    end_range = index_range
    selection_indices = []

    for i in range(no_of_selections):
        random_index = random.randint(start_range, end_range)
        selection_indices.append(random_index)
        start_range = end_range
        end_range = end_range + index_range
    random.shuffle(selection_indices)
    return (selection_indices)

quicksort_input_array = generate_item_list()
randomizedselect_input_array = quicksort_input_array.copy()
random_select_list = random_select_list()

# ###################################
print("General (1 000 000): ")
delta_t1 = quicksort.sort_by_quicksort(quicksort_input_array, random_select_list)
print(delta_t1)
print("\n")


####################################
print("Randomized (1 000 000): ")
delta_t2 = randomized_select.select_by_randomizedselect(randomizedselect_input_array, random_select_list)
print(delta_t2)
print("\n")


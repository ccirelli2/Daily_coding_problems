


L = [1,4,3,5,6,3,6,7]


def problem_9(list_obj):
   
    # Length of list_object
    len_obj = len(list_obj)

    # List Capture Final Sums
    List_sums = []

    # Create Range Object Using Len of List Object
    '''
    Purpose:    The below for loop runs from 0 up to the len of the list object
                This will establish the position that we start at in the list
                and ensure that we iterate over every possible combination.
    '''
    for index_pos in range(0, len_obj):
    
        # Redefine List Object w/ new start position
        list_obj = list_obj[index_pos:]
   
        # List Capture Intermediary Values
        List_capture_intermediary_values = []

        # Create New Range Object w/ Step 
        for value in range(0, len(list_obj), 2):

            # Append Each Value to Intermediary List
            List_capture_intermediary_values.append(list_obj[value])
           
        # Take Sum of Intermediary List
        List_sums.append(sum(List_capture_intermediary_values))

   
    return max(List_sums)



# Run Code
highest_sum_non_adjacent_num_in_list = problem_9(L)

print(highest_sum_non_adjacent_num_in_list)








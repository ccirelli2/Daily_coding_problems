# Import Modules
import random



# Create List of Randomly Generated Integers
def gen_list_ran_ints(num_ints, min_weight, max_weight):
        random.seed(3)
        list_weights = []
        for x in range(0, num_ints):
                list_weights.append(random.randint(min_weight, max_weight))
        return list_weights



def get_combinations(ran_weights):
    ''' Input: List of random numbers.
        Output: List of lists.  All combinations of numbers. 
    '''
    
    # List to capture lists of combinations
    a = []

    # Iterate over range of 0 to length of weights. 
    for iteration in range(0, len(ran_weights)):

        # Get Combintaions
        for step in range(0, len(ran_weights)):
            a.append(ran_weights[0: step+1])
 
        # Rotate List so pos0 is not at the end
        pos_0 = ran_weights[0]
        ran_weights.remove(pos_0)
        ran_weights.append(pos_0)
       
    return a


def get_optimal_combo_boat_n(list_all_combos):
    ''' Input:  List of lists.  All possible combinations of weights
        Output: Tuple
                (combo_length, combo_sum, combo_list)
        Purpose: Find the optimal combination with the longest length and
                 highest sum less than 201. 
    '''
    Count = 0
    combo_list = []

    # Iterate Through All the Weight Combinations
    for combo in list_all_combos:

        # If Count is 0 and Sum < 201, then we combo_list is empty

        if Count == 0 and sum(combo) < 201:
            combo_list.append((len(combo), sum(combo), combo))
            Count =+1

        # If the count is > 0, then we have a value appended to the list to compare.
        elif Count > 0 and sum(combo) < 201:

            prior_combo_len = combo_list[0][0]
            prior_combo_sum = combo_list[0][1]

            # If the Length of the Current Combo is > then prior, remove prior and append new.
            if len(combo) > prior_combo_len:
                combo_list.remove(combo_list[0])
                combo_list.append((len(combo), sum(combo), combo))
                Count +=1

            # If the lengths are equal, check which has the lower sum
            elif len(combo) == prior_combo_len:

                # If the sum of the new one is >, then replace prior with new combo.
                if sum(combo) > prior_combo_sum:
                    combo_list.remove(combo_list[0])
                    combo_list.append((len(combo), sum(combo), combo))
                    Count +=1
                # If the sum is equal or less, then lets do nothing as they are equivalent.
                else:
                    Count +=1

    # Return Combo list
    return combo_list


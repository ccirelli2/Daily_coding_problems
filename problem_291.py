'''
Good morning! Here's your coding interview problem for today.

This problem was asked by ---

An imminent hurricane threatens the coastal town of Codeville and the people of Codeville are fat. 

If at most two fat people can git in a rescue both 
and the maximum weight limit for a given boat is k, 
determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three. 
'''
'''
    Objective:  Find the combination of weights that results in the least number
                of life boats required. 
                Max weight per boat is 200
    Approach    Start with the first number in the list.  
                Iterate the list starting with index value 1 and add it to the first number. 
                If the sum is < 200, continue adding integers. 
                If equal to 200, append the combination to a list holding combos. 
                If greater than 200, append the first number to the list of combos. 

    Step1:      Is the weight > 200 - min_weight?
                If so, no other people can fit in the boat and the weight be < 200.
                Therefore, one boat has been occupied an we should remove this person 
                from the list. 
                Append the weight to the list and move to the next one. 

    Step2:      If weight < 200 - min_weight, then there may be an additional person that
                can fit in the life raft.
                We will want to look at every possible combination of the first weight in the
                list with every other weight starting from position 1:, excluding first weight. 

    Step2B:         

'''

# Import Modules
import random
import problem_291_module as m1


# Weight Limitations
min_weight = 8
max_weight = 200
num_people = 100


# Generate List of Random Weights. 
ran_weights = m1.gen_list_ran_ints(num_people, min_weight, max_weight)

# List of Optimal Weight Combinations
optimal_weights = []


# Loop Over Range w/ Len Ran Weights
while len(ran_weights) > 0:
    
    # Get All Possible Combinations of Weights
    a = m1.get_combinations(ran_weights)

    # Get Optimal Combination
    b = m1.get_optimal_combo_boat_n(a)            
    optimal_weights.append(b)

    
    # Remove Weights in Optimal Boat from List of Random Weights
    'b is a list inside of which is a single tuple (len, sum, combo_list)'
    try:
        for weight in b[0][2]:
            ran_weights.remove(weight)
    
    except IndexError:
        print('Index Error')


print(len(optimal_weights))
print(optimal_weights)























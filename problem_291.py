#!/usr/bin/env python3
'''
Good morning! Here's your coding interview problem for today.

This problem was asked by ---

An imminent hurricane threatens the coastal town of Codeville and the people of Codeville are fat.

If at most two fat people can git in a rescue both
and the maximum weight limit for a given boat is k,
determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.
'''

# Import Modules
import problem_291_module as m1


# Weight Limitations
min_weight = 8
max_weight = 200
num_people = 100

# Generate List of Random Weights.
rand_weights = m1.gen_list_ran_ints(num_people, min_weight, max_weight)

tests = [
    {'list': [100, 200, 150, 80], 'limit': 200, 'minNumberOfBoats': 3},
    {'list': [100, 100, 100, 100], 'limit': 200, 'minNumberOfBoats': 2},
    {'list': [1, 1, 1, 1], 'limit': 200, 'minNumberOfBoats': 1},
    {'list': [1], 'limit': 200, 'minNumberOfBoats': 1},
    {'list': [200], 'limit': 200, 'minNumberOfBoats': 1},
    {'list': [200, 200], 'limit': 200, 'minNumberOfBoats': 2},
    {'list': [200, 200, 200], 'limit': 200, 'minNumberOfBoats': 3},
    {'list': [200, 200, 200, 200], 'limit': 200, 'minNumberOfBoats': 4},
    {'list': [199, 200, 1, 1], 'limit': 200, 'minNumberOfBoats': 3},
    {'list': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'limit': 200, 'minNumberOfBoats': 1},
]


def run(ran_weights):
    # List of Optimal Weight Combinations
    optimal_weights = []

    # Loop Over Range w/ Len Ran Weights
    while ran_weights:

        # Get All Possible Combinations of Weights
        a = m1.get_combinations(ran_weights)

        # Get Optimal Combination
        b = m1.get_optimal_combo_boat_n(a)
        optimal_weights.append(b)

        # Remove Weights in Optimal Boat from List of Random Weights
        # b is a list inside of which is a single tuple (len, sum, combo_list)
        try:
            for weight in b[0][2]:
                ran_weights.remove(weight)

        except IndexError:
            print('Index Error')

    # print(optimal_weights)
    return len(optimal_weights)


for test in tests:
    result = run(test['list'])
    assert result == test['minNumberOfBoats']
    print(result)

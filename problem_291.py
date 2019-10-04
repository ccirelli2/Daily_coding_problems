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
import random


# Create List of Randomly Generated Integers

def gen_list_ran_ints(num_ints, lower, upper):
	list_weights = []
	for x in range(0, num_ints):
		list_weights.append(random.randint(lower, upper))
	return list_weights

list_rand_nums = gen_list_ran_ints(100, 8, 200)
























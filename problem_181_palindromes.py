# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 07:36:30 2019

@author: Chris.Cirelli


PROBLEM-------------------------------------------------------------------------------------
Given a string, split it into as few strings as possible such that each string is a palindrome.
For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].
Given the input string abc, return ["a", "b", "c"]
"""




def get_rev_order_list(test_list):
    # Object 4 Reverse List
    rev_order_list = []
    len_list = len(test_list)
    # Create a Sequence That Iterates 0 - len(list) in reverse order    
    for x in range(len_list-1, -1, -1):
        # Append to rev_order_list each value in list that coincides to index = x
        rev_order_list.append(test_list[x])
    # Return Original List in reverse
    return (rev_order_list)


def driver_function(test_string):
    
    # Convert String to List
    t1_list = list(test_string)
    
    # Object to hold identified palindromes
    palindromes = []

    # Create Sequence that will constitute the upper range of our step for iterating the list
    for step in range(0, len(t1_list) + 1):
    
        # Count - Used to lower range value forward by 1 step
        count = 0
    
        # Create Sequence to Generate Combos
        for num in range(0, len(t1_list)):
            # Append Letter Combo If len() == Step
            letter_combo = t1_list[count: count + step]
            
            # See Documentation. Only Consider Letter Combos w/ Len == Step & >1 
            if len(letter_combo) == step and len(letter_combo) > 1:
                # Get Reverse of Combo
                rev_combo = get_rev_order_list(letter_combo)
            
                # Test if letter combo == rev_combo
                if rev_combo == letter_combo:
                
                    if letter_combo not in palindromes:
                        palindromes.append(letter_combo)
                
            # Increase Count
            count +=1
            
    # If No Matches
    if len(palindromes) == 0:
        return t1_list
    else:
        # Return Palindromes
        return palindromes


test_string = 'anna'

test = driver_function(test_string)

print(test)




    
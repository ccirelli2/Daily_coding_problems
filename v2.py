# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 19:32:07 2019

@author: Chris.Cirelli
"""


# Check if Palidrome
def get_rev_order(string):
    
    # Check if single letter
    if len(string) == 1:
        return string
    
    else:
        # Convert String to List
        list_string= list(string)
        # Object 4 Reverse List
        rev_order_list = []
        len_list = len(list_string)
        
        # Create a Sequence That Iterates 0 - len(list) in reverse order    
        for x in range(len_list-1, -1, -1):
            # Append to rev_order_list each value in list that coincides to index = x
            rev_order_list.append(list_string[x])
    # Return Original List in reverse
    return (rev_order_list)



# DRIVER FUNCTION-------------------------------------------------------------

def driver_function(string):
    len_string = len(string)
    list_string = list(string)
    
    # Intermediary List of Palidrome
    intermed_palidrome = []

    # Create Step Starting at 0
    for step in range(0, len_string):
    
        # Iterate String:
        for letter in range(step + 1, len_string + 1):    
                
            letter_combo = list_string[step:letter]
            rev_letter_combo = get_rev_order(letter_combo)
            
            # Check if Palidrome exists
            if letter_combo == rev_letter_combo:
            
                # If letter == 1
                if letter == 1 and len(letter_combo) != 0:
                    intermed_palidrome.append(letter_combo)
                    
                # If not the first letter of the sequence, check to see if palidrome overlaps + is longer
                # than the preceding palidrome.  Overlaps means that the first letter of the next palidrome is
                # in the first palidrome.
                # anna!frank
                else:
                    # Establish index position of last letter of the last palidrome added to list
                    num_char_list_palidromes = sum([len(x) for x in intermed_palidrome]) - 1
                    # If my present step is less than the last index position of the last appended palidrome, then 
                    # I know there is overlap. Therefore, and if there is overlap, I should not append a new palidrome 
                    #whose length is less than the preceding palidrome if there is overlap
                
                    # If smaller, then there is overlap.  Therefore, we should not append a new palidrome whose len
                    # is less than the preceding palidrome
                    #elif step < num_char_list_palidromes and len(letter_combo) < len(intermed_palidrome[-1]):
                    #    pass
                
                    # If smaller, and longer than the preceding palidrome, then we need to replace the last
                    # palidrome with the letters that don't overlap as one value in the list, and then add the palidrome
                    if step <= num_char_list_palidromes and len(letter_combo) > len(intermed_palidrome[-1]):
                        
                        # Step 1:  Isolate the last palidrome
                        last_palidrome = intermed_palidrome[-1]
                        # Step 2: Drop last palidrome from the list
                        intermed_palidrome.remove(last_palidrome)
                        # Step3:  Append the piece that overlaps with the new palidrome
                        len_new_palidrome = len(letter_combo) * -1
                        overlap           = last_palidrome[0 : len_new_palidrome]
                        if len(overlap) != 0:
                            intermed_palidrome.append(overlap)
                        # Step4:  Append New Palidrome to list
                        intermed_palidrome.append(letter_combo)
                    
                    
                    # what about if the step is greater? Then we don't need to check the length as there is no overlap. 
                    elif step > num_char_list_palidromes:
                        intermed_palidrome.append(letter_combo)
                    
    return intermed_palidrome



                    
string = 'racecarannakayak'

test = driver_function(string)                    

print(test)
                
            
            
            
    





        
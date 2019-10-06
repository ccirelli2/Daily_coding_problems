# PROBLEM
'''
Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
'''


list1 = [9,9]
list2 = [5,2]

one_list = [list1]
two_list = [list1, list2]


def stupid_problem(obj_list):
    'Function only takes a list or list of lists'
    num_lists = len(obj_list)

    list1_reorder = []
    list2_reorder = []
    list3_reorder = []

    # Function For One List
    if num_lists == 1:
        # Define List1
        list1 = obj_list[0]
        # Iterate List 1
        for i in range(1, len(list1)+1):
            # Append Values in Reverse Order to List1_reorder
            list1_reorder.append(list1[i*-1]) 
        return int(''.join([str(x) for x in list1_reorder]))
    
    # Two Lists
    elif num_lists == 2:
        # Define Lists
        list1 = obj_list[0]
        list2 = obj_list[1]
        # Define Length of Lists
        r1 = range(1, len(list1) +1)
        r2 = range(1, len(list2) +1)
        # Reorder List1 and List2 (returns list object)
        for i, j in zip(r1, r2):
            list1_reorder.append(list1[i*-1])
            list2_reorder.append(list2[j*-1])
        # Convert list1_reorder & list2_reorder back to ints
        list1_reorder_int = int(''.join([str(x) for x in list1_reorder]))
        list2_reorder_int = int(''.join([str(x) for x in list2_reorder]))
        sum_list1_2 = list1_reorder_int + list2_reorder_int
        # Reorder sum_list_2
        str_sum_list1_2 = str(sum_list1_2)
        list5 = []
        for i in range(1, len(str_sum_list1_2)+1):
            list5.append(str_sum_list1_2[i*-1])
        
        list5_int = int(''.join([str(x) for x in list5]))

        return list5_int
        

test1 = stupid_problem(two_list)
print(test1)











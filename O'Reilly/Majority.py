"""
We have a List of booleans. Let's check if the majority of elements are true.

Some cases worth mentioning:

an empty list should return false;
if trues and falses have an equal amount, function should return false.
Input: A List of booleans.

Output: A Boolean.

Example:

is_majority([True, True, False, True, False]) == True
is_majority([True, True, False]) == True
"""



# Solution #1

import numpy as np

def is_majority(lst:list) -> bool:
    try:
        return sum(lst)/len(lst) > 0.5
    except ZeroDivisionError:
        return False
    
if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
    



    
 # Solution #2
 
def is_majority(lst:list) -> bool:
    return lst.count(True) > lst.count(False)

if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
 
    
  
"""
Check if the given number is even or not. Your function should return True if the number is even, and False if the number is odd.

Input: An int.

Output: A bool.

Example:

is_even(2) == True
is_even(5) == False
is_even(0) == True
How it’s used: (math is used everywhere)

Precondition: both given ints should be between -1000 and 1000
"""



# Solution #1

def is_even(number:int) -> bool:
    return number%2 == 0

if __name__ == '__main__':
    print('Example:')
    print(is_even(2) == True)
    
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")    



# Solution #2

def is_even(number:int) -> bool:
    return number & 1 == 0 # unmber bitwise & 1 gives {0 - odd, 1 - even}

if __name__ == '__main__':
    print('Example:')
    print(is_even(2) == True)
    
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")    
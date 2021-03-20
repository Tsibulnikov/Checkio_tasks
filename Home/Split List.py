"""
You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements. If it has no elements, then two empty arrays should be returned.

Input: Array.

Output: Array or two arrays.

Example:

split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3]) == [[1, 2], [3]]
"""



# Solution #1

def split_list(lst:list) -> list:
    empty = []
    l = len(lst)
    half = int(l/2)
    if (l > 0) and (l % 2 == 0):
        empty.append(lst[:half])
        empty.append(lst[half:])
    elif (l > 0 ) and (l % 2 != 0):
        empty.append(lst[:half+1])
        empty.append(lst[half+1:])
    return empty

if __name__ == '__main__':
    print('Example:')
    print(split_list([1, 2, 3, 4, 5, 6]))
    print(split_list([1, 2, 3]))
    



    
 # Solution #2
 
def split_list(items:list) -> list:
    half = (len(items) + 1) // 2
    return [items[:half], items[half:]]

if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    
  
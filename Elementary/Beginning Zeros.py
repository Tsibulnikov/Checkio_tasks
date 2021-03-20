"""
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.

Output: An Int.

Example:

beginning_zeros('100') == 0
beginning_zeros('001') == 2
beginning_zeros('100100') == 0
beginning_zeros('001001') == 2
beginning_zeros('012345679') == 1
beginning_zeros('0000') == 4
"""



# Solution #1

def beginning_zeros(string):
    cnt = 0
    for i in string:
        if int(i) == 0:
            cnt += 1
        else:
            return cnt
    return cnt
if __name__ == '__main__':
    print('Example:')
    print(beginning_zeros('100'))
    
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4

# Solution #2

def beginning_zeros(string):
    return len(string) - len(string.lstrip('0'))

if __name__ == '__main__':
    print('Example:')
    print(beginning_zeros('100'))
    
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4

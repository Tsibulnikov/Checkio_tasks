'''
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string. Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
Output: A string.

Example:

between_markers('What is >apple<', '>', '<') == 'apple'
between_markers('No[/b] hi', '[b]', '[/b]') == 'No'
How it is used: for parsing texts

Precondition: can't be more than one final marker and can't be more than one initial. Marker can't be an empty string
'''



# Solution #1

from difflib import SequenceMatcher

def between_markers(text:str, marker1:str, marker2:str) -> str:
    if (marker1 in text) and (marker2 in text) and (text.index(marker1) > text.index(marker2)):
        return ''
    else:
        if marker1 in text:
            string1 = text[text.index(marker1) + len(marker1):]
        else:
            string1 = text
        if marker2 in text:
            string2 = text[:text.index(marker2)]
        else:
            string2 = text
        #print('str1:', string1, 'str2:', string2)
        match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
        #print(match)
        return (string1[match.a:match.a + match.size])

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    assert between_markers("No <hi> one",">","<") == ''
    print('Wow, you are doing pretty good. Time to check it!')
    



    
 # Solution #2
 
def between_markers(text:str, begin:str, end:str) -> str:
    return text.split(begin)[-1].split(end)[0] if (text.find(begin) <= text.find(end)) or text.find(end) == -1 else ''
    
if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    
        # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    assert between_markers("No <hi> one",">","<") == ''
    print('Wow, you are doing pretty good. Time to check it!')
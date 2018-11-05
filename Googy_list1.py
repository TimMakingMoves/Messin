"""
Googy_list.py
Developer: Tim Weiser
Project: Googy_list1.py
Date: 11/4/2018
References:
https://developers.google.com/edu/python/exercises/basic
https://www.w3schools.com/python/ref_list_sort.asp
https://docs.python.org/3/howto/sorting.html

Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0
Google's Python Class
http://code.google.com/edu/languages/google-python-class/
"""


def match_ends(words):
    """
    A function that, given a list of strings, returns the count of the number
    of strings where the string length is 2 or more and the first and last
    chars of the string are the same size.
    :param words: a list of strings that are 2 or more characters long
    :return: a printed string in the format noted above
    :rtype: str
    """
    number_of_strings_that_match = 0
    for test_string in words:
        if len(test_string) >= 2:
            if test_string[0] == test_string[-1]:
                number_of_strings_that_match = number_of_strings_that_match + 1
    return number_of_strings_that_match


def front_x(words):
    """
    A function that, given a list of strings, sorts the strings alphabetically, but sorts those that start with x first.
    :param words: a list of strings that are 2 or more characters long
    :return: a printed string in the format noted above
    :rtype: str
    """
    x_strings = []
    non_x_strings = []
    for list_entry in words:
        if list_entry[0] == 'x':
            x_strings.append(list_entry)
        else:
            non_x_strings.append(list_entry)
    x_strings.sort()
    non_x_strings.sort()
    output_string = x_strings + non_x_strings
    return output_string


def sort_last(tuples):
    """
    A function that, given a list of tuples, sorts the tuples based on their last indexed value.
    :param list tuples: a list of tuples that each contain 2 or more values.
    :return: a printed string in the format noted above
    :rtype: str
    """
    sorted_tuples = sorted(tuples, key=lambda tuple_values: tuple_values[-1])
    return sorted_tuples


def test(got, expected):
    """
    Simple provided test() function used in main() to print what each function returns vs. what it's supposed to return.
    :param list got: the output of the above function that is being tested
    :param list expected: the output we are hoping our functions are creating
    :return: OK or X if the test did or didn't work, as well as the inputs and outputs of the functions tested.
    :rtype: str
    """
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    """
    Calls the above functions with interesting inputs. prints out the function names if everything goes smoothly!
    """
    print
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    """
    Standard boilerplate to call the main() function.
    """
    main()

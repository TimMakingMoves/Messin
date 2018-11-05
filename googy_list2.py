"""
googy_list2.py
Developer: Tim Weiser
Project: Messin
Date: 11/4/2018
References:
https://developers.google.com/edu/python/exercises/basic
https://stackoverflow.com/questions/12934190/is-there-a-short-contains-function-for-lists
https://docs.python.org/2.3/whatsnew/section-enumerate.html

Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0
Google's Python Class
http://code.google.com/edu/languages/google-python-class/
"""


def remove_adjacent(nums):
    """
    Function that, given a list of numbers, return a list where
    all adjacent == elements have been reduced to a single element,
    so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.
    :param list nums: A list of numbers, some repeated.
    :return: a printed string in the format noted above
    :rtype: list
    """
    entries_list = []
    for number in nums:
        if number not in entries_list:
            entries_list.append(number)

    return entries_list


# Below is a secondary solution that manipulates the list passed in, not creating a new one.

#    for number in nums:
#        if nums.count(number) > 1:
#            nums.remove(number)

#    return nums


def linear_merge(list1, list2):
    """
    Function that, given two lists sorted in increasing order, create and return a merged
    list of all the elements in sorted order. You may modify the passed in lists.
    Ideally, the solution should work in "linear" time, making a single
    pass of both lists.
    :param list nums: A list of numbers, some repeated.
    :return: a printed string in the format noted above
    :rtype: list
    NOTE: I'm not happy with this answer, but I'm putting linearity on my list of things to-learn.
    """
    big_list = list1 + list2
    return sorted(big_list)


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


# Calls the above functions with interesting inputs.
def main():
    """
    Calls the above functions with interesting inputs. prints out the function names if everything goes smoothly!
    """
    print 'remove_adjacent'
    test(remove_adjacent([1,2, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == "__main__":
    """
    Standard boilerplate to call the main() function.
    """
    main()

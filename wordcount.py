"""
Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

Google's Python Class
http://code.google.com/edu/languages/google-python-class/

wordcount.py
Developer: Tim Weiser
Project: Messin (Learning Python Scripts)
Date: 11/11/2018
References:
https://docs.python.org/2/library/stdtypes.html#typesmapping
https://www.youtube.com/watch?v=haycL41dAhg
https://stackoverflow.com/questions/4842956/python-how-to-remove-empty-lists-from-a-list?noredirect=1&lq=1
https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
"""

import string


def split_words(filename):
    """
    Function that takes the input of a filename, and returns a list of all of the words in that file in an ordered list.
    NOTE: The solution given by Google is below, commented out.
    :param string filename: path of a txt file
    :return: list of ordered lowercase words
    :rtype: list
    """
    f = open(filename, 'rU')
    all_text = f.read()
    f.close()
    split_text = all_text.split()
    lowercase_split_text_punc = [item.lower() for item in split_text]
    lowercase_split_text = sorted([''.join(c for c in s if c not in string.punctuation) for s in
                                   lowercase_split_text_punc])
    lowercase_split_text_full = [x for x in lowercase_split_text if x]
    return lowercase_split_text_full


def make_dict_of_word_count(list_of_words):
    """
    Function that takes in a list of words in str format and puts them into the keys of a dictionary, with the values
    being the number of times that key word shows up in the original string.
        NOTE: Those if/and statements get pretty confusing, because I didn't know you could access a dictionary's
    value after it was already set- otherwise I'd just create one list of words and increment each key's value like in
    the Google-provided solution.
    :param list list_of_words: list of a bunch of strings of all words in the above file
    :return: dict each word in the file and the value of how many times it is repeated
    :rtype: dict
    """
    list_of_non_duplicate_words = []
    count_dict = {}
    word_count = 0
    for word in list_of_words:
        if len(list_of_non_duplicate_words) > 0 and list_of_non_duplicate_words[-1] == word:
            word_count = word_count + 1
        elif len(list_of_non_duplicate_words) == 0 or list_of_non_duplicate_words[-1] != word:
            if len(list_of_non_duplicate_words) > 1:
                count_dict[list_of_non_duplicate_words[-1]] = word_count
            word_count = 1
            list_of_non_duplicate_words.append(word)
    return count_dict


def print_word_count(word_count_dict):
    """
    Function that takes in a dictionary of words in {str:int} format and prints them
    :param dict word_count_dict: dictionary of the word count of a file
    """
    word_list = []
    for word in word_count_dict:
        words = '{} {}'.format(word, str(word_count_dict[word]))
        word_list.append(words)
        print words


"""
def google_solution(filename):
    # Utility used by count() and Topcount().
    word_count = {}  # Map each word to its count
    input_file = open(filename, 'r')
    for line in input_file:
        words = line.split()
        for word in words:
            word = word.lower()
            # Special case if we're seeing this word for the first time.
            if not word in word_count:
                word_count[word] = 1
            else:
                word_count[word] = word_count[word] + 1
    input_file.close()  # Not strictly required, but good form.
    return word_count
"""


def main():
    """
    Gives us our file path and goes through each function in order- getting the words, putting them into a dict,
    and printing the list out.
    """
    filename = 'C:\Users\Timby\Documents\Freelance\python\hlice.txt' #full text of Alice in Wonderland
    word_list = split_words(filename)
    words_dict = make_dict_of_word_count(word_list)
    print_word_count(words_dict)


if __name__ == '__main__':
    """
    Standard boilerplate to call the main() function.
    """
    main()

"""
input.py
Developer: Tim Weiser
Project: String Mixup
Date: 11/1/2018
References:
https://www.youtube.com/watch?v=tKTZoB2Vjuk
https://stackoverflow.com/questions/3411771/multiple-character-replace-with-python
https://www.youtube.com/watch?v=tKTZoB2Vjuk
"""


def dr_evil(dollar_amt):
    """
    Function takes an integer and outputs a string in the format "int dollars", unless it is 1 million, then it adds
    the string " (pinky)" to the end of it.
    :param int dollar_amt: number of dollars you want to output
    :return: a printed string in the format noted above
    :rtype: str
    """
    if dollar_amt == 1000000:
        result = '{} {} {}'.format(str(dollar_amt), 'dollars', '(pinky)')
    else:
        result = '{} {}'.format(str(dollar_amt), 'dollars')

    return result


def fix_start(word_to_star):
    """
    Function takes an input string, notes the first letter of that string, then replaces subsequent appearances
    of that character them with '*'
    :param str word_to_star: a string with repetitions of the first letter of that word.
    :return: a printed string in the format noted above
    :rtype: str
    """
    letter_to_star = word_to_star[0]
    end_of_word = word_to_star[1:]
    starred_end = end_of_word.replace(letter_to_star,'*')
    result = letter_to_star + starred_end

    return result


def mix_up(first_word, second_word):
    """
    Function takes 2 input strings, pops off the first 2 letters of each word and switches them, outputting a singular
    string with both words with a space in between them.
    :param str first_word: the first word to mix up
    :param str second_word: the second word to mix up
    :return: a printed string in the format noted above
    :rtype: str
    """
    first_two_letters_word_1 = first_word[0:2]
    rest_of_word_1 = first_word[2:]
    first_two_letters_word_2 = second_word[0:2]
    rest_of_word_2 = second_word[2:]
    new_word_1 = first_two_letters_word_2 + rest_of_word_1
    new_word_2 = first_two_letters_word_1 + rest_of_word_2
    result = '{} {}'.format(new_word_1, new_word_2)

    return result


def main():
    """
    Function tests inputs of the above functions and double checks if we get the outputs we are targeting.
    A successful run of this function will print the names of the above functions.
    """
    print 'dr_evil'
    assert dr_evil(10) == '10 dollars'
    assert dr_evil(42) == '42 dollars'
    assert dr_evil(1000000) == '1000000 dollars (pinky)'

    print 'fix_start'
    assert fix_start('babble') == 'ba**le'
    assert fix_start('aardvark') == 'a*rdv*rk'
    assert fix_start('google') == 'goo*le'

    print 'mix_up'
    assert mix_up('mix', 'pod') == 'pox mid'
    assert mix_up('dog', 'dinner') == 'dig donner'
    assert mix_up('gnash', 'sport') == 'spash gnort'

if __name__ == "__main__":
    # Standard boilerplate to call the main() function.
    main()

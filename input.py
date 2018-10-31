"""
input.py
Developer: Tim Weiser
Project: Calculator
Date: 10/30/2018
References:
https://www.youtube.com/watch?v=rfscVS0vtbw
"""


def addition(number_1, number_2):
    """
    Function adds 2 numbers together and prints out a string
    :param float number_1: First number to be added
    :param float number_2: Second number to be added
    :return: a printed string of the numbers added together as well as their sum
    :rtype: str
    """
    sum_1 = float(number_1) + float(number_2)
    result = '{} + {} is {}'.format(str(number_1).strip(), str(number_2).strip(), str(sum_1))
    return result


def main():
    """
    Main execution of the program when script is ran
    """

    number_1 = raw_input("What is the first number you want to add?")
    number_2 = raw_input("What is the number you want to add to " + number_1 + "?")

    sum_1 = addition(float(number_1), float(number_2))

    print sum_1


if __name__ == "__main__":
    # execute only if run as a script
    main()

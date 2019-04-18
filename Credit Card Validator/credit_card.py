"""
Python script to check validity of credit card numbers
Author : ThePythonDjango.Com
Functions : usage, get_cc_number, sum_digits, validate
URL : https://github.com/anuragrana/Python-Scripts/blob/master/credit_card_validator.py

Python script to check credit card vendor
Author : adelq
Functions : card name/number constants, identify_card_type
URL : https://github.com/adelq/card_identifier/blob/master/card_identifier/card_issuer.py

<Credit Card Numbers>
URL : https://www.paypalobjects.com/en_AU/vhelp/paypalmanager_help/credit_card_numbers.htm

<Luhn Algorithm>
URL : https://en.wikipedia.org/wiki/Luhn_algorithm

<Credit card INN numbers>
URL : https://en.wikipedia.org/wiki/Payment_card_number
"""

import sys


# Card name constants
AMEX = 'AMEX'
DISCOVER = 'Discover'
MASTERCARD = 'MasterCard'
VISA = 'Visa'
UNKNOWN = 'Unknown'

# Card number constants (IIN ranges)
AMEX_2 = ('34', '37')
MASTERCARD_2 = ('51', '52', '53', '54', '55')
DISCOVER_2 = '65',
DISCOVER_4 = '6011',
VISA_1 = '4',


def usage(): # run through terminal
    msg = """

        usage:
        python3 credit_card_validator credit_card_number

        example:
        python3 credit_card_validator 34678253793


    """
    print(msg)


def get_cc_number(): # creates a list from command line input
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    return sys.argv[1]


def sum_digits(digit): # Finds the sum of digits of a number until the sum becomes a single digit (finds the check digit)
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum


def validate(cc_num):
    # reverse the credit card number
    cc_num = cc_num[::-1]
    # convert to integer
    cc_num = [int(x) for x in cc_num]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9, eg if the value is 14 take away 9 the new value is now = 5
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    # return True or False
    return sum_of_digits % 10 == 0


def identify_card_type(card_num):
    """
    Identifies the card type based on the card number.
    This information is provided through the first 6 digits of the card number.
    Input: Card number, int or string
    Output: Card type, string
    # >>> identify_card_type('370000000000002')
    'AMEX'
    # >>> identify_card_type('6011000000000012')
    'Discover'
    # >>> identify_card_type('5424000000000015')
    'MasterCard'
    # >>> identify_card_type('4007000000027')
    'Visa'
    # >>> identify_card_type('400700000002')
    'Unknown'
    """

    card_type = UNKNOWN
    card_num = str(card_num)

    # AMEX
    if len(card_num) == 15 and card_num[:2] in AMEX_2: # if the card is 15 characters in length
        card_type = AMEX # then the card is an AMEX card

    # MasterCard, Visa, and Discover
    elif len(card_num) == 16: # if the card is 16 characters in length then the card is either a Mastercard, Visa or Discover
        # MasterCard
        if card_num[:2] in MASTERCARD_2: # if the card number begins with MASTERCARD_2 = ('51', '52', '53', '54', '55')
            card_type = MASTERCARD # then the card is a Mastercard

        # Discover
        elif (card_num[:2] in DISCOVER_2) or (card_num[:4] in DISCOVER_4): # if the card number begins with DISCOVER_2 = '65', DISCOVER_4 = '6011'
            card_type = DISCOVER # then the card is a Discover

        # Visa
        elif card_num[:1] in VISA_1: # if the card number begins with VISA_1 = '4'
            card_type = VISA # then the card is a Visa

    # VISA
    elif (len(card_num) == 13) and (card_num[:1] in VISA_1): # if the card is 13 characters in length
        card_type = VISA # then the card type is also a Visa

    return card_type # return the card type, if the card type doesn`t match any card types listed then the card type is unknown

# prints whether the card is valid (boolean = True/False) and card vendor (identify_card_type)
if __name__ == "__main__":
    print(validate(get_cc_number()))
    print(identify_card_type(get_cc_number()))

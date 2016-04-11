# -*- coding: utf-8 -*-
__author__ = "karnikamit"

'''
1. Define a function which takes a string as its argument.
   It should print the characters of the string one at a time.
   First solution should use a while loop and the second solution should implement a For loop
'''

# Soln 1


def print_chars_while(string):
    i = len(string)
    j = -1
    while abs(j) < i+1:
        print string[j]
        j -= 1


# Soln 2


def print_chars_for(string):
    for char in string[::-1]:
        print char
    else:
        return 'Done!'


'''
2. Enhance the above function with a second argument to the function.
'''


def print_chars_while2(string, reverse=False):
    i = len(string)
    if reverse:
        j = -1
        while abs(j) < i+1:
            print string[j]
            j -= 1
    else:
        j = 0
        while i:
            print string[j]
            i -= 1
            j += 1
    return 'Reversed: %s' % reverse


def print_chars_for2(string, reverse=False):
    if reverse:
        string = string[::-1]
    for char in string:
        print char
    return 'Reversed: %s' % reverse

'''
3. Define a function which will accept a string as argument and return True
   if the string is a palindrome. Palindrome is a word in English which when read backwards from the last letter
   to first spells the   same. example:- Madam, Radar, Solos etc
'''


def palindrome_check(string):
    return string == string[::-1]


'''
4. Create a dictionary with keys as strings and values as integers.
   List the keys in alphabetical order.
   List the values from lower to higher
'''


def list_keys_values_asc():
    a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    a_dict_keys = sorted(a_dict.keys(), key=lambda x: x[0], reverse=False)
    dict_values = []
    dict_values.extend(a_dict.values())
    dict_values.sort()
    re_response = {'keys in alphabetical order': a_dict_keys,
                   'values from lower to higher': dict_values}
    return re_response


'''
5. Take a dictionary as input and create another dictionary by inverting the keys and values.
   ie, the values becomes the key and the keys become the values.
'''


def invert_dict(ipdict):
    opdict = dict()
    # op_dict = {value: key for key, value in ipdict.iteritems()} # python 2.6 does not support dict comprehensions
    for key, value in ipdict.iteritems():
        opdict[value] = key
    return opdict

# -*- coding: utf-8 -*-
__author__ = "karnikamit"

'''
1. Recursive fn to get factorial of a number
'''


def fact(n):
    if n == 1:
        return 1
    return n*(fact(n-1))

'''
2. Reverse a list recursively
'''
rev_list = []


def reverse(arg):
    if not arg:
        return rev_list
    if isinstance(arg, list):
        rev_list.append(arg.pop())
    # For a string
    elif isinstance(arg, str):
        rev_list.append(arg[-1])
        arg = arg[:-1]
    return reverse(arg)

'''
3. Write a recursive function to compute the Fibonacci sequence
'''


def fib(n):
    if 0 < n < 3:
        return 1
    return fib(n-1) + fib(n-2)


def fib_seq(n): return [fib(i) for i in xrange(1, n+1)]

'''
4. Implement a solution to the Tower of Hanoi.
'''


def ihanoi(n, source, helper, target):  # n = no of disks
    if n > 0:
        ihanoi(n-1, source, target, helper)
        if source:
            target.append(source.pop())
        ihanoi(n-1, helper, source, target)
    return 'source: {0}, helper: {1}, target: {2}'.format(source, helper, target)

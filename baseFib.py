#!/usr/bin/env python3

"""
    Program that transforms a natural number in its unique Fibonacci
    representation.
"""

import numpy as np


def checkIntPositive(n):
    """ Ensures that the input n is a positive integer. """
    if int(n) != n:
        raise TypeError("%s is an invalid positive int value" % n)
    elif n < 0:
        raise ValueError("%s is an invalid positive int value" % n)
    return n


def argumentManager():
    """ Manager to get the n input. """
    return checkIntPositive(float(input()))


def displayHash(vect_repr):
    """ Prints the number in hash format.

    Argument:
        vect_repr (numpy array): Representation of the number in a certain base.
    """
    print("#".join([str(num) for num in vect_repr]))


def baseFib(n):
    """ Returns the Fibonnaci representation of the input n number.

    Parameter:
        n (int): Natural number.

    Returns:
        fib_repr (numpy array): Fibonacci representation of n as an array.
    """
    fib_repr = np.zeros(shape=1, dtype=int) # allows case n = 0

    num_iter = 0
    n_mem = 0
    while n != n_mem:
        remainder = n - n_mem
        k = 0
        f_n = 0
        f_n_plus_1 = 1
        value = 0
        while remainder >= value:
            k += 1
            # update the Fibonacci numbers
            tmp = f_n_plus_1
            f_n_plus_1 += f_n
            f_n = tmp
            value = f_n_plus_1

        # update the memory in order to know the following remainder
        n_mem += f_n

        # fill the vector representation of n (if first row, create it first)
        if num_iter == 0:
            fib_repr = np.zeros(shape=(k-1), dtype=int)
        fib_repr[k-2] = 1
        num_iter += 1

    return fib_repr[::-1]



if __name__ == "__main__":
    # get the arguments needed
    n = argumentManager()

    # compute the Fibonnaci representation of n
    fib_repr = baseFib(n)
    displayHash(fib_repr)

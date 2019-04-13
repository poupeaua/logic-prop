#!/usr/bin/env python3

"""
    Program that transforms a natural number in its unique factorial
    representation.
"""

from tools import *


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

    return fib_repr



if __name__ == "__main__":
    # get the arguments needed
    args = argumentManager()

    # compute the Fibonnaci representation of n
    fib_repr = baseFib(args.n)
    displayHash(fib_repr)

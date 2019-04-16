#!/usr/bin/env python3

"""
    Program that transforms a natural number in its unique factorial
    representation.
"""

from tools import *


def baseFact(n):
    """ Returns the factorial representation of the input n number.

    Parameter:
        n (int): Natural number.

    Returns:
        fact_repr (numpy array): Factorial representation of n as an array.
    """
    fact_repr = np.zeros(shape=1, dtype=int) # allows case n = 0

    num_iter = 0
    n_mem = 0
    while n != n_mem:
        remainder = n - n_mem
        k = 0
        factorial = 1
        value = 0
        while remainder >= value:
            k += 1
            a_k = 0
            factorial *= k
            while remainder >= value and a_k <= k-1:
                a_k += 1
                value = a_k * factorial

        # if a_k = 1 we need to go back to a previous factorial (except if k=1)
        if a_k == 1 and k != 1:
            factorial = int(factorial/k)
            k -= 1
            a_k = k
        else:
            a_k -= 1

        # update the memory in order to know the following remainder
        n_mem += a_k * factorial

        # fill the vector representation of n (first iteration create it first)
        if num_iter == 0:
            fact_repr = np.zeros(shape=(k+1), dtype=int)
        fact_repr[k] = a_k
        num_iter += 1

    return fact_repr



if __name__ == "__main__":
    # get the argument needed
    n = argumentManager()

    # compute the factorial representation of n and display it
    fact_repr = baseFact(n)
    displayHash(fact_repr)

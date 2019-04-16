"""
    Tools file used to stock useful functions used in other files.
"""

# import useful libraries
import numpy as np
# import argparse # program arguments manager


def checkIntPositive(n):
    """ Ensures that the input n is a positive integer. """
    if int(n) != n:
        raise TypeError("%s is an invalid positive int value" % n)
    elif n < 0:
        raise ValueError("%s is an invalid positive int value" % n)
    return n


def argumentManager():
    """ Manager to get the n input. """
    # parser = argparse.ArgumentParser(description="Process some natural number.")
    # parser.add_argument("-n", type=checkIntPositive, required=True,
    #     help="Natural number")
    # args = parser.parse_args()
    return checkIntPositive(float(input()))


def displayHash(vect_repr):
    """ Prints the number in hash format.

    Argument:
        vect_repr (numpy array): Representation of the number in a certain base.
    """
    vect_repr = list(vect_repr[::-1])
    print("#".join([str(num) for num in vect_repr]))

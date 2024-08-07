#!/usr/bin/env python

"""
This is an example of a job that calculated the sum of squares until 1,000,000
"""

import sys


def main():
    """ main entry point """
    print("starting...")
    sys.stdout.flush()
    my_sum = 0
    for i in range(1000000000):
        my_sum = my_sum + i * i
    print(my_sum)


if __name__ == "__main__":
    main()

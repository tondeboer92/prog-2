#!/usr/bin/env python3

#include <cstdlib>

from person import Person
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt


@njit
def fib_numba(n):
        if n <= 1:
                return n
        else:
                return(fib_numba(n-1) + fib_numba(n-2))



def fib_py(n):
        if n <= 1:
                return n
        else:
                return(fib_py(n-1) + fib_py(n-2))




def main():
    x = []
    y = []
    for n in range(35,39):
        start = pc()
        fib_py(n)
        end = pc()
        print(f"Process took {round(end-start)} seconds")
        x.append(n)
        y.append(round(end-start))
    print(x)
    print(y)
    plt.plot(x,y)
    plt.savefig("Fig1")

if __name__ == '__main__':
	main()


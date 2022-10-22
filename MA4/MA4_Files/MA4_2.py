#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc


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
	f = Person(5)
	start1 = pc()
	print(f.get())
	fib_py(f.get())
	end1 = pc()
	print(f"Process took {round(end1-start1, 2)} seconds")
	start2 = pc()
	print("numba")
	fib_numba(f.get())
	end2 = pc()
	print(f"Process took {round(end2-start2, 2)} seconds")
	start3 = pc()
	print("person")
	f.fib()
	end3 = pc()
	print(f"Process took {round(end3-start3, 2)} seconds")

if __name__ == '__main__':
	main()

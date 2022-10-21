#!/usr/bin/env python3

from person import Person
from numba import njit



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
	start2 = pc()
	print("numba")
	fib_numba(f.get())
	end2 = pc()
	start1 = pc()
	print("person")
	f.fib()
	end1 = pc()

if __name__ == '__main__':
	main()

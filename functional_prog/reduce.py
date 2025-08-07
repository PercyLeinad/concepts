'''
Python's reduce() is a function that implements a mathematical technique called folding or reduction. 
reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value. 
Python's reduce() is popular among developers with a functional programming background, but Python has more to offer.
'''
from functools import reduce

def reduce_fun(i,j):
    return i * j

def square_num(*nums):
    return reduce(reduce_fun,nums)

print(square_num(2,3,4,5))

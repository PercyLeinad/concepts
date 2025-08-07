'''
The built-in filter() function in Python is used to process an iterable and extract items that satisfy a given condition, as determined by a filtering function.
filter() returns an iterator that yields only the elements for which the filtering function returns a truthy valu
'''
def filter_fun(i):
    return i % 2 == 0

def even_num(*nums):
    return list(filter(filter_fun,nums))

print(even_num(2,3,4,5))

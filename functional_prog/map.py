'''
The built-in map() function in Python allows you to apply a transformation function to each item of one or more iterables, producing an iterator that yields transformed items.
This function is particularly useful for processing and transforming data in a functional programming style without explicitly using a for loop. 
Here’s an example of using map() to square numbers in a list:
'''
def map_fun(i):
    return i ** 2

def square_num(*nums):
    return list(map(map_fun,nums))

print(square_num(2,3,4,5))






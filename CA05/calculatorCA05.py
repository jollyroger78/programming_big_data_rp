import math

def sum(a, b):
    return map(lambda x, y: x + y, a, b)
    
def subtract(values):
    return reduce(lambda x, y: x-y, values)
    
def multiply(values):
    return reduce(lambda x, y: x*y, values)
    
def divide(a, b):
    return map(lambda x, y: x/float(y) if y != 0 else 'error', a, b)

def power(values):
    return reduce(lambda x, y: x**float(y), values)
    
def sqrt(a):
	return map(lambda x: x ** (1/2.0), a)
    
def is_even(values):
	return filter(lambda x: x%2 == 0, values)
	
def fizzbuzz(values): 
    return filter(lambda x: x%3==0 and x%5==0, values)
    
def pythagorean(n):#as generator
	for x in range(1,n):
		for y in range(x,n):
			for z in range(y,n):
				if x**2 + y**2 == z**2:
					yield (x,y,z)

pyt = pythagorean(50)
for v in pyt:
    print 'Pythagorean as generator\n', v,

#as list comprehension
pythagorean = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]	
print 'Pythagorean as list comprehension: \n', pythagorean


#tests
print 'Sum: ', sum([15, 7, 47, 5], [45, 34, 12, 1])
print 'Subtract: ', subtract([20, 76, 8])
print 'Multiply: ', multiply([2, 4, 6])
print 'Division: ', divide([2, 4,6], [3, 5, 0])
print 'Power: ', power([3, 3, 2])
print 'Square root: ', sqrt([2, 3, 4, 5]) 
print 'Even Values: ', is_even([20, 10, 5, 33, 98])
print 'FizzBuzz: ', fizzbuzz([15, 34, 30, 100, 9, 20, 60])


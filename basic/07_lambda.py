## 1 #######################################################################################
cube = lambda n:n ** 3

print(cube(8))

## 2 #######################################################################################

nums = [4,8,12,16,20]

doubles = list(map(lambda x:x * 2,nums))

print(doubles)

people = ["Darcy","Christina","Dana","Annabel"]

peeps = map(lambda name:name.upper(),people)

print(peeps);

## 2 #######################################################################################

## Write a function called drecement_list that accepts a single list of numbers as a parameter.
## however,should return a list.You can either pass map another name function or use a lambda.
## A lambda is preferable, even if it is a litle scary looking.

## define the function decrement_list that accepts a list called
def drecement_list(values):
    ## The lambda returns val-1 for each val in the list
    return list(map(lambda val:val-1,values))


print(drecement_list([1,2,3]))

## 3 #######################################################################################

## Write a function called remove_negatives that accepts a list of numbers and returns a copy
## of the list with all negative numbers removed.Use filter() in your implementation,not a list
## comprehension!

def remove_negatives(num):
    return list(map(lambda n:n,filter(lambda v: v >= 0,num)))


print(remove_negatives([-1,3,4,-99]))
print(remove_negatives([-7,0,1,2,3,4,5,]))
print(remove_negatives([50,60,70]))

## 4 #######################################################################################
## Implement a function is_all_string that accepts a single iterable and return True if it 
## contains ONLY string. Otherwise,it should return false 

def is_all_string(values):
    return all([type(val) == str for val in values])


print(is_all_string(['a']))

## 5 #######################################################################################
## Write a function called extremes Which accepts an iterable.It should return a tuple containig
## the minimum and maximum elements 

def extremes(val):
    return(min(val),max(val));


print(extremes((99,25,30,-7)))
print(extremes([1,2,3,4,5]))
print(extremes("alcatraz"))

## 6 ###########################################################################################
## Write a function max_magnitude that accepts a single list full of numbers. It should return the
## number with the largest magnitude(the number that is furthest away from zero).

def max_magnitude(num):
    return max(abs(val) for val in num)


print(max_magnitude([300,20,-900]))


## 7 ###########################################################################################
## Write a function called sum_even_values.This function should accept a variable number of arguments
## and return the sum of all the arguments that are divisible by 2. If there are no number divisible by 2
## the function should return 0. To be clear,it accepts all the numbers as individual arguments!


def sum_even_values(numbers):
    sum = 0
    for n in numbers:
     if n % 2 == 0:
      sum = sum + n
    return sum
    return 0         

print(sum_even_values([1]))


## 8 ###########################################################################################
## Write a function called sum_floats. This function should accept a variable number of arguments
## The function should return the sum of all the parameters that are floats. If there are no floats
## the function should return 0


def sum_floats(*args):
  return sum(arg for arg in args if type(arg) == 'float')

 


print(sum_floats(1.5,2.4,'awesome',[],1))


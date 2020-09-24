## 01  Write a function called product that accepts two parameneters and returns
## the products of the two parameters (multiply them together).

def product(x,y):
    return x*y


print(product(2,-2))

#############################################################################################
## 02 Write a function called return_day. This function takes in one parameter
## (a number from 1 - 7) and returns the day of the week (1 is Sunday,2 is Monday etc.)
## If the number is less than 1 or greater than 7, the function should return None.

def return_day(n):
    
    days = [[1,"Sunday"],[2,"Monday"],[3,"Tuesday"],[4,"Wednesday"],[5,"Thurday"],[6,"Friday"],[7,"Saturday"]]

    for d in days:
        if n == d[0]:
         return d[1:]
    return None

print(return_day(3))

#############################################################################################
## 03 Write a function called last_element. This fuction takes in one paramenter (a list) and returns the last
## value in the list. It should return None if the list is empty.

def last_element(ls):
    for e in ls:
        return ls[-1:]
    return None
         
print(last_element([]))

#############################################################################################
## 04  Write a function called number_compare. This function takes in two parameters (both numbers). If the first
##  is greater than the second, this function return "First is greater" if the second number is greather than
##  the first,the fuction return "Second is greater"
##  Otherwise the function returns "Numbers are equal"


def number_compare(x,y):
    if x > y:
        return 'First is greater'
    elif y > x:
        return 'Second is greater'
    
    return 'Numbers are equal'
    
print(number_compare(4,4))

#############################################################################################
## 05 Write a function called single_letter_count. This function takes in two parameters (two string). The
## first paramenter should be a word and the second should be a letter. The function return the number
## of times that letter appears in the word. The function should be case insensitive. If the letter is not
## found in the word, the function should return 0

def single_letter_count(w,l):
        return w.lower().count(l.lower())

result = single_letter_count("hello","l")
print(result)




#############################################################################################
## 06  Write a function called multiple_letter_count. This function takes in one parameter (a string)
## and returns a dictionary with the keys being the letters and the values being the count()

def multiple_letter_count(word):
    return {w:word.count(w) for w in word}


print(multiple_letter_count("awesome"))

#############################################################################################
## 07 Write a function called list_manipulation. This function take in four parameters (a list,command,location and value)
## if the command is "remove" and the location is "end,the fuction should remove the last value in the list and return
## the value removed
## if the command is "remove" and the location is "beginning",the function should remove the first value in the list and
## return the value removed
## If the command is "add" and the location is "beginning" the function should add the value (fourth parameter) to the
## beginning of the list and return the list
## If the command is "add" and the location is "end", the function should add value the value (fourth parameter) to the
## end of the list and return the list


def list_manipulation(ls,comd,loc,val):
    if comd == "remove" and loc == "end":
              return ls.pop(-1)
    if comd == "remove" and loc == "beginning":
              return ls.pop(0)
    if comd == "add" and loc == "beginning":
       ls.insert(0,val)
    return ls
    if comd == "add" and loc == "end":
       ls.append(val)
    return ls   

print(list_manipulation([1,2,3],"add","end",30))

############################################################################################
## 08 Write a function called is_palindrome. A Palindrome is a word,pharse,number,or other sequence
## of characters which reads the same backward or forward. This function should take in one parameter
## and returns TRUE or FALSE depending on whether it is a palindrome.As a bonus, allow your function to
## ignore whitespace and capitalization so that is_palindrome return True.


def is_palindrome(nm):
    if nm == nm[::-1]:
        return True
    return False

print(is_palindrome("amanaplanacanalpanama"));

#################################################################################################
## 09 Write a function called frequency. This function accepts a list a search_term(this will always be a primitive value) and
## returns the number of time the search_term appears in the list

def frequency(num,n):
    return num.count(n)
x = frequency([1,2,3,4,4,4],4)

print(x)


#################################################################################################
## 10 Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the
## product of all even numbers in the list.



def multiply_even_numbers(even):
    y=1
    for x in even:
        if x % 2 == 0:
           y *= x
    return y

print(multiply_even_numbers([1,2,3,4,5,6]))

##########################################################################################
## 11 Write a function called CAPITALIZE.This function accepts a string and returns the same
## string with the first letter capitalized. 

def capitalize(string):
    return string[0].upper()+string[1::]


print(capitalize("jamaica"))


##########################################################################################
## 12 Write a function callecd compact. This function accepts a list and returns a list of
## value s that are truthy values,without any of the falsey values

def compact(values):
     true_list = []
     for val in values:
          if val:true_list.append(val)    
     return true_list 
     
print(compact([0,1,2,"",[],False,None,"Al done"]))

##########################################################################################
## 13 Write a function called intersection. This function should accept two list and return
## a list with the values that are in both input lists

def intersection(x,y):
    combine = []
    for v1 in x:
        for v2 in y:
            if v1 == v2:
                combine.append(v1)
    return combine

print(intersection(['a','b','z'],['x','y','z'])) 

############################################################################################



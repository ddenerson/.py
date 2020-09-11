## Given two list ["CA","NJ","RI"] and ["Calirfonia","New Jersey","Rhode Island"]
## create a dictionary that looks like this {'CA' :'California','NJ': 'New Jersey','RI':'Rhode Island'}

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]


combine = {list1[l]:list2[l] for l in range(3)}

print(combine)


## Give a person variable:
## person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
## Create a dictionary called answer, that makes each first item list a key
## and the second item a corresponding value. Just look at the end goal:
## {'name':'jared',job : 'Musician', 'city': 'Bern'}

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

info = {dt[0]:dt[1] for dt  in person}

print(info)

## Create a dictionart with the key as vowel in the alphabet and the value as 0.
## Your dictionary shuould look like this {'a':0,'e':0,'i':0,'o':0,'u':0}

letters = "aeiou"
key = 0

vowels = dict.fromkeys(letters,0)

## OR

vowel = {l:0 for l in 'aeiou'}
print(vowels)
print(vowel)

## Your task is to create dictionart that maps ASCII keys to their corresponding letters.
## Use a dictionary comprehension and chr().Save the result to the answer variable.You only
## need to care about capital letters (65-90)
    
ch = {w:chr(w) for w in range(65,90)}

print(ch)
    












## Define a function contains_purple that accepts any number of arguments.It should return
## TRUE if any of the arguments are "purple"(all lowercase).Otherwise, it should return False


def contains_purple(*args):
    
    for arg in args:
        if arg == "purple":
            return True
    return False

print(contains_purple("green",False,37,"blue","hello world"))

## Write a function called combine_words which accepts a single called word and any number
## of additional key word arguments. If a prefix is provided, return the prefix followed
## by the world. If a suffix is provided, return the world followed by the suffix. If neither
## provided,just return the world. It might sound confusing,but the examples should make this a
## a lot clearer


def fucao_teste(*args):
    s = 0
    for x in args:
        s +=x
        print(x)   
    


nums = [1,2,3,4,5,6]
print(fucao_teste(*nums))


names = ["Elie","Tim","Matt"]
capital_w = []

for word in names:
    capital_w.append(word[0])
print(capital_w)

print("##################################################")

numbers = [1,2,3,4,5,6]

even = [n for n in numbers if n % 2 == 0]
print(even);

print("##################################################")

nameII = [n[::-1].lower() for n in ["Ellie","Tim","Matt"]]
print(nameII)
    
print("##################################################")

list1 = [1,2,3,4]
list2 = [3,4,5,6]

answer = [n for n in list1 if n in list2]
print(answer)

print("##################################################")           

divisible = [x for x in range(1,100) if x % 12 == 0]

print(divisible)

print("##################################################")

string = [w for w in "amazing" if w not in ["a","e","i","o","u"]]
print(string)

print("##################################################")

nested = [[n for n in range(3)] for x in range(0,3)]

print(nested)

print("##################################################")

nestedII = [[n for n in range(10)] for x in range(10)]

print(nestedII)


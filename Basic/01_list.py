
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]

people[0] = "Hannah"
people[0].upper()

print("#########################################")


colors = ["purple","teal","magenta"]

for color in colors:
    print(color)

print("#########################################")

numbers = [1,2,3,4]
i = 0

while i < len(numbers):
    print(numbers[i])
    i +=1

print("#########################################")

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ' ' 

for sound in sounds:
    result += sound.upper()


print(result)

print("#########################################")

instructors = []

instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")

for i in instructors:
    print(i)

print("#########################################")

instructor = []

instructor.extend(["Colt","Blue","Lisa"])

for x in instructor:
    print(x)

print("#########################################")

instructor.pop(2)
instructor.pop(0)
instructor.insert(0,"Done")

for x in instructor:
    print(x)



    

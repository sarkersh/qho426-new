# https://youtu.be/MuK3ggxQK9A
# xargs :- It works like tuples
def student(id, name):
    print(id, name)
student(101, "Shakil")

def student(*details):
    print(details[0])

student(101, "Shakil", 3.75)

def add(num1,num2):
    sum = num1 + num2
    print(sum)
add(10,20)
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
add(10,20,30,40,50)

# xxargs :- It work like dictionary as key , value pair
def student(id,name):
    print(id,name)
student(101,"Skakil Sarker")

def stud(**details):
    print(details)
    print(details["id"])
stud(id=101, name="Shakil sarker")
"""
Intro to files
"""
### Piece 1
### you may find this piece of code on the internet:
f = open("hello.txt", "r")
print(f.read())
f.close()
### Piece 2
## which is equivalent to this:
file_location = "hello.txt"
file_pointer = open(file_location, "r")
file_content = file_pointer.read()
print(file_content)
### Piece 3
### and also to this:
print(open("hello.txt", "r").read())
### Piece 4
### final template:
file_pointer = open("hello.txt", "r")
file_content = file_pointer.read()
print(file_content)
file_pointer.close()
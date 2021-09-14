# link filename (string) to a file on the disk
file_pointer = open("hello.txt", "r")
# file_pointer is now a handler which points to that file
# now, read the whole content of the file
# into a single string variable file_content
file_content = file_pointer.read()
# print the whole content of the file as a single string
print(file_content)
print("~~~~~~~~~~~~~~~~~~~")
# convert string file_content into array of strings
w = file_content.split("\n")
# w is now an array (list)
print(w)
print("~~~~~~~~~~~~~~~~~~~")
# iterate for the array w
for hi in w:
    #print(hi)
    if (hi !=''):
        print(hi)
   #else:
    #    print("-hohoho-")
file_pointer.close()
# there are two main types of loop statements in python:
# FOR (aka foreach) and WHILE
# FOR is used when you know exactly how many times to repeat an action
# (i.e. as many as items in a list)
# WHILE is used when you don't know how many time to repeat an action
# (i.e. until user inputs a valid number, or until user chooses EXIT)
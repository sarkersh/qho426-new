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
# initialise the counter
counter = 0
# iterate for the array w
for hi in w:
    #print(hi)
    if (hi != ''):
        print(hi)
        counter = counter + 1
    #else:
    #    print('-hohoho-')
print("~~~~~~~~~~~~~~~~~~~")
print("Total no of lines:", len(w))
print("No of non-empty lines:", counter)
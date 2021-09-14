"""
Activity 2: Reading a File
We can read a file by simply providing a file path, absolute or relative, to the function open. For example,
if we wish to read the file named data.txt that is stored in the current working directory then we can do the following:
file = open("locations.txt")
It is important to close a file once we are done processing it so as to free it for use by other processes.
We can do this simply by using the method close:
file.close()
1. We can also use the keyword with in order to automatically close a file once we are done processing it.
2. We can read the entire content of the file as a string using the method read. This will read in all the data
including any white space and/or end of line (\n) characters.
3. We can use the method split of string to divide the string into separate lines and
remove any end of line (\n) characters.
4. We can also read only a few characters by supplying an appropriate value to the method "read(10)":
5. It is often useful to retrieve all the lines in a file as a list using the method "readlines".
6. Note that this will also read in the end of line (\n) character which can be removed using the method "strip"
7. Alternatively, we can loop through the file line by line. Note that this will include the end of line character (\n).
of string on each line:
"""
#with open("locations.txt") as file:
    #data = file.read()
    #print(data)
    #lines = data.split("\n")
    #print(lines)
    #partial_data = file.read(10)
    #print(partial_data)
    #lines = file.readlines()
    #print(lines)
    #line = file.readline().strip()
    #print(line)
    #for line in file:
        #print(line)
        #print(line.strip()) # line.strip() will remove any white space including the \n character
#######################Task#############################################################################################

def search(file_path):
    print("Searching...")
    with open(file_path) as file:
        for line in file.readlines():
            print(f"Looked in {line.strip()}")
    print("...Done")
def run():
    search("locations.txt")

run()






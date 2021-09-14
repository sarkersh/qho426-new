"""
Activity 1: Current Working Directory
It is often useful to check our current working directory before beginning to work with files so that we can provide
appropriate file paths.  We can do this using the method "getcwd" of the module "os" which displays the file path of the
current working directory.

import os
path = os.getcwd()
print(f"Current Working Directory: {path}")
We can also display the content of this directory using the method "listdir" of the module "os" as follows:
for file in os.listdir(path):
    print(file)
#~~~~~~~~~~~~~~~~Task~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"""
import os
def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following:")
    for file in os.listdir(path):
        print(file)
def run():
    print("Processing...")
    cwd()
run()



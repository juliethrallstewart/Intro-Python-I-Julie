"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open('foo.txt', 'r')
print(f.read())
f.close()
print(f.closed)


# note using a "with" statement will automatically close the file
with open('foo.txt') as fl:
    print(fl.read())
    



# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# Python allows you to read, write and delete files.
# Use the function open("filename","w+") to create a file. ...
# To append data to an existing file use the command open("Filename", "a")
# Use the read function to read the ENTIRE contents of a file.
# Use the readlines function to read the content of the file one by one.

# YOUR CODE HERE
# new_file = open('bar.text', 'w')

with open('bar.txt', 'w+') as new_file:
    new_file.write("did I open my new file correctly? \n" 
                    "I certainly hope so! \n" 
                    "here goes a test!")

with open('bar.txt', 'r') as new_file:
    print(new_file.read())

append_f = open('bar.txt', 'a+')
append_f.write("Yay! it worked! \n"
        "But is this how you append new lines in the file?")
append_f.close()

with open('bar.txt', 'r') as new_file:
    print(new_file.read())



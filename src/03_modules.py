"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import fileinput

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv[0], "sys args [0]")

args = [arg for arg in sys.argv]
print(args)

for arg in sys.argv:
    print(arg, "arg in sys.argv")

#iterates over the files listed in sys.argv[1:]
# for line in fileinput.input():
#     process(line)



print(len(sys.argv), "this is the length")
print(str(sys.argv), "the arguments")

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print out the OS platform you're using:
# YOUR CODE HERE

print(os)

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())



print(os.uname())
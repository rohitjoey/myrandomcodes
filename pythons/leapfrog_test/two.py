# The function is expected to return a string.
# The function accepts string as parameter.

import math


def logic(my_input):
    # Write your code here and remove pass statement
    # Don't print anything. Just return the intended output
    # You can create other functions and call from here
    length = len(my_input)
    out = ""
    loop = math.floor(length /4)
    print(loop)
    for i in range(0,loop):
        front = my_input[4*i+2]+my_input[4*i+3]
        back = my_input[4*i]+my_input[4*i+1]
        out += front+back
    for i in range(4*loop,length):
        out+= my_input[i]
    return out


# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic(my_input))

# The function is expected to return a string.
# The function accepts string as parameter.

import math


def logic(my_input):
    punctuation = ['.',',',':',';','?','!']
    out=""
    text = my_input.split(" ")
    for char in text:
        temp = char[1:]
        punc = ""
        for i in temp:
            if i in punctuation:
                punc+=i
            else:
                out+=i
        out+=char[0]+'arg'
        out+=punc+" "        

    return out
   



# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic(my_input))

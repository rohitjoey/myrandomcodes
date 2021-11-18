def cleanFloor(my_input):
    my_output=[]
    for char in my_input:
        # print(char,i)
        if char in ("d","u","s","t"):
            my_output.append("")
        else:
            my_output.append(char)
    if "".join(my_output) == my_input:
        return "It is a clean floor"
    else:
        return "".join(my_output)



my_input = input("Enter the string: ")

print(cleanFloor(my_input))

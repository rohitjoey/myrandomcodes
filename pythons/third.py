def miniPeaks(my_input):
    # print(my_input)
    n=len(my_input)
    # print(n)
    my_output=[]
    for i,num in enumerate(my_input):
        # print(type(i))
        if not((i == 0) or (i== n-1)):
            if num>my_input[i-1] and num>my_input[i+1]:
                my_output.append(num)


    return my_output



my_input = [1, 2, 3, 4, 5, 6]

print(miniPeaks(my_input))

# [1, 2, 1, 1, 3, 2, 5, 4, 4]
# [4, 5, 2, 1, 4, 9, 7, 2]
# [1, 2, 3, 4, 5, 6]

def logic(my_input):
    # Write your code here and remove pass statement
    # Don't print anything. Just return the intended output
    # You can create other functions and call from here
    sCount = my_input.count('s')
    if not sCount:
        return "Yes"
    else:
        count = 0
        for i, char in enumerate(my_input):
            if char == 's':
                if my_input[i+1] == 's':
                    count+=1
        if count>=2:
            
            return "Yes"
        else:
            return "No"
    
# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic(my_input))

def brackets(exp):
    count = 0
    stack=[]
    for char in exp:
        if char in ("(","{"):
            stack.append(char)
        else:
            if not stack:
                count+=1
            else:
                current = stack.pop()
                if current == '(':
                    if char != ')':
                        count+=1
                if current == '{':
                    if char != '}':
                        count+=1
        # print(stack)
        # print(count)
    
    if stack:
        count= len(stack)
    return count



print(brackets(exp="(()){{}(}}}}"))
 

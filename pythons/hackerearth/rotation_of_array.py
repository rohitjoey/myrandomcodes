def rotation_of_array(a,k):

    # print(a)
    
    n=len(a)
    while k:
        last=a[n-1]
        for i in range(n-1,-1,-1):
            a[i]=a[i-1]
        a[0]=last    
        
        # print(a)   
        
        k-=1
    
    for i in range(0, n):    
        print(a[i],end=" ")

test_case_input = int(input())
for i in range(0, test_case_input):
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()][:n]

rotation_of_array(a,k)

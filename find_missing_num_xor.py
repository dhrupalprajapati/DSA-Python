def XOR(a,b):
    if a == b:
        return 0
    elif a == 0:
        return b
    else:
        return a

arr = list(map(int,input().rstrip().split()))

# n = arr[-1]

# complete_arr = list(range(1,n+1))

i = 0
while i < len(arr):
    
    i += 1
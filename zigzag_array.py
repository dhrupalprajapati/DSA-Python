# Zig-zag array is:  5 10 8 12 6 9 4 -> 5 < 10 > 8 < 12 > 6 > 9 < 4
# <><><><><>(Zigzag pattern) OR ><><><><><(zig zag pattern)

arr = list(map(int,input().rstrip().split()))

i = 0
flag = True

#while loop
while (i < len(arr)-1):
    if flag == True:
        if arr[i] < arr[i+1]:
            # increment i and change flag here because we have used continue ...
            i += 1
            flag = not flag 
            continue
        else:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
        if arr[i] > arr[i+1]: #comarition 
            i += 1
            flag = not flag
            continue
        else:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    # this is excuted when flag = 0,1 and condition if false and else part excuted ...
    i += 1
    flag = not flag
print(*arr)

arr = list(map(int,input().rstrip().split()))

start,end = 0, len(arr)-1

# start < len(arr)//2 and end > len(arr)//2
while  start < end:
    arr[start],arr[end] = arr[end],arr[start]
    start += 1
    end -= 1
    
print(*arr)
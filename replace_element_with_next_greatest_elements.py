arr = list(map(int,input().rstrip().split()))

max_from_right = arr[len(arr)-1]

for i in range(len(arr)-2,-1,-1):
    if max_from_right > arr[i]:
        arr[i] = max_from_right
    else:
        max_from_right = arr[i]

print(*arr)
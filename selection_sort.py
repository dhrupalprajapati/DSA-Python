arr = list(map(int,input().rstrip().split()))

for fixed in range(0,len(arr)):
    for var in range(fixed+1,len(arr)):
        if arr[fixed] > arr[var]:
            arr[fixed], arr[var] = arr[var], arr[fixed]

print(*arr)

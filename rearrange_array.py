# rearrange such that arr[j] is i if arr[i] is j

arr = list(map(int,input().rstrip().split()))

temp = list(range(len(arr)))

for i in range(len(arr)):
    temp[arr[i]] = i

arr = temp.copy()
print(*arr)
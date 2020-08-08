# assume array contains only entries for 0's and 1's

arr = list(map(int,input().rstrip().split()))
count_0 = arr.count(0)
count_1 = len(arr) - count_0

for i in range(len(arr)):
    if i < count_0:
        arr[i] = 0
    else:
        arr[i] = 1
        
print(*arr)
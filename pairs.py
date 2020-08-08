arr_len, key = list(map(int,input().rstrip().split()))
arr = list(map(int,input().rstrip().split()))

# arr.sort()
c = 0
for i in range(arr_len):
    for j in range(arr_len):
        if arr[i] - arr[j] == key:
            c += 1
print(c)
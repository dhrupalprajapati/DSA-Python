arr = list(map(int,input().split()))

# uses O(n) extra spaces
non_duplArr = []
for i in range(len(arr)-1):
    # print(i,arr[i])
    if arr[i] != arr[i+1]:
        non_duplArr.append(arr[i])

non_duplArr.append(arr[-1])
print(non_duplArr)
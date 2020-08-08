arr1 = list(map(int,input().rstrip().split()))
arr2 = list(map(int,input().rstrip().split()))

len_arr1 = len(arr1)
len_arr2 = len(arr2)

i,j = 0,0
res_arr = []
while i < len_arr1 and j < len_arr2:
    if arr1[i] < arr2[j]:
        res_arr.append(arr1[i])
        i += 1
    else:
        res_arr.append(arr2[j])
        j += 1

while i < len_arr1:
    remain_arr = arr1[i:]
    res_arr += remain_arr
    break

while j < len_arr2:
    remain_arr = arr2[j:]
    res_arr += remain_arr
    break

print(res_arr)
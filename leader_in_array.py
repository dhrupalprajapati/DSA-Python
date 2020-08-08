# O(n) time complexity using Max from right as mfr

arr = list(map(int,input().rstrip().split()))

mfr = arr[-1]
print(mfr)
for i in range(len(arr)-2,-1,-1):
    if arr[i] >= mfr:
        print(arr[i])
        mfr = arr[i]

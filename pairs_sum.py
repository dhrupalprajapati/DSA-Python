arr = list(map(int,input().rstrip().split()))
g_sum = int(input())
arr.sort()

l,r = 0, len(arr)-1

while l < r:
    if arr[l] + arr[r] < g_sum:
        l += 1
    elif arr[l] + arr[r] > g_sum:
        r -= 1
    else:
        # when arr[l] + arr[r] == g_sum
        print(arr[l], arr[r])
        l += 1 # or do r -= 1
    

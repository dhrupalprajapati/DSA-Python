# find missing num whithin series started from 1 to n...

arr = list(map(int,input().rstrip().split()))
n = arr[-1]

sum_n = (n * (n+1))/2
sum_arr = sum(arr)
print(int(sum_n-sum_arr))
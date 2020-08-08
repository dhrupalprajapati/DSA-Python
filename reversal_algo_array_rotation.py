arr = list(map(int,input().rstrip().split()))
rev = int(input())

reverse_arr = arr[:len(arr)-rev][::-1] + arr[-rev:][::-1]
print(*reverse_arr[::-1])
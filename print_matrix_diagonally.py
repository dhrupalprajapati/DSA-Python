arr = [
    ['a','b','c','d','e'],
    ['f','g','h','i','j'],
    ['k','l','m','n','o'],
    ['p','q','r','s','t']
]
# m * n
m = 4
n = 5

for k in range(0,m):
    i, j = k, 0
    while i >= 0:
        print(arr[i][j],end=" ")
        i -= 1
        j += 1
    print()

for k in range(1,n):
    i, j = m-1, k
    while j <= n-1:
        print(arr[i][j],end=" ")
        i -= 1
        j += 1
    print()


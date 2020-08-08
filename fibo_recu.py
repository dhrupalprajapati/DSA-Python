def fibo(no):
    if no <= 1:
        return no
    else:
        return fibo(no-1) + fibo(no-2)

ip = int(input())
for i in range(ip):
    print(fibo(i),end=" ")
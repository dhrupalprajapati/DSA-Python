def fibo(no):
    if no <= 1:
        return no
    else:
        return fibo(no-1) + fibo(no-2)

inp = int(input())
for no in range(0,inp):
    print(fibo(no),end=" ")

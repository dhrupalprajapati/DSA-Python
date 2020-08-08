def fibo(no):
    if no > 0:
        if no == 1:
            print(0)
        else:
            fst, sec = 0, 1
            print(fst, sec, end=" ")
            for i in range (2,no):
                next = fst + sec
                fst, sec = sec, next
                print(next,end=" ")
    else:
        raise IndexError

no = int(input())
fibo(no)

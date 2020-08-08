from math import sqrt

def primeCheck(no):
    if no < 2:
        return False
    # elif no == 2 or no == 3:
        # return True
    elif no % 2 == 0:
        return False
    else:
        for i in range(3,int(sqrt(no))+1,2):
            if no % i == 0:
                return False
        else:
            return True

no = int(input())
print(primeCheck(no))
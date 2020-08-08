no = int(input())

def check_prime(no):
    if no <= 1:
        return "Not Prime"
    elif no == 2 or no == 3:
        return "Prime"
    else:
        for i in range(3,int(no**0.5)+1,2):
            if no % i == 0:
                return "Not Prime"
        return "Prime"

print(check_prime(no))
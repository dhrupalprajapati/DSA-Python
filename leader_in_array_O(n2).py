# leader means element having it's all right side occurances ar less then that element.
# last element is also a leader because no element occur behind that, i.e. the last one.

arr = list(map(int,input().rstrip().split()))

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        print(arr[i], arr[j])
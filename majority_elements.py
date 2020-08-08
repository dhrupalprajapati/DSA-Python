# majority means if there are n no. of elements then occurance of element > n / 2 is Majority element.

arr =  list(map(int,input().rstrip().split()))

majority_no = len(arr) // 2
count = {}

for i in arr:
    # if key exists then increment value of particular key
    if i in count: 
        count[i] += 1
    # if key doesn't exists then add key-value pair.
    else:
        count[i] = 1
    if count[i] > majority_no:
        print(i, count[i])    
else:
    print("Majority elements not found.")
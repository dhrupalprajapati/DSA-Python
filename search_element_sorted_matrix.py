arr = [
    [10,20,30,40],
    [12,22,33,45],
    [14,24,44,47],
    [16,26,46,50]
]

# i is pointing to 1st row and j is pointing to last column
i,j =0,3
last = arr[i][j]
search = 16

while i < len(arr) and j >= 0:
    if search  == arr[i][j]:
        print(f"Fount at: arr[{i}][{j}]")
        break
    else:
        if search < arr[i][j]:
            j -= 1
        else:
            i += 1
else:
    print("Not Found")
arr = [10, 20, 30, 40, 50]
rev_arr = []
for i in range(len(arr)-1, -1, -1):
    x = arr[i]
    rev_arr.append(x)

print(arr)
print(rev_arr)

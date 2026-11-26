# code to add 2 arrays using for loop
arr1 = [10, 20, 30, 40, 50]
arr2 = [1, 2, 3]
arr3 = []
for i in range(min(len(arr1), len(arr2))):
    temp = arr1[i]+arr2[i]
    arr3.append(temp)
print(arr3)

# code to find the maximum value from an array without using in-built function
arr = [12, 45, 7, 89, 23, 56]
max_num = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_num:
        max_num = arr[i]
print(max_num)

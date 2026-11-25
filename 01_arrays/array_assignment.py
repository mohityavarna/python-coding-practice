# code to add 2 arrays using for loop
arr1 = [10, 20, 30, 40, 50]
arr2 = [1, 2, 3]
arr3 = []
for i in range(len(min(arr1, arr2))):
    temp = arr1[i]+arr2[i]
    arr3.append(temp)
print(arr3)

size = int(input("enter the length of array"))
arr = []
for i in range(size):
    x = int(input("enter the next value"))
    arr.append(x)  # appending the elements to arr variable
print("original list", arr)

index = int(input("enter the index value you want to delete"))
i = index
while i < size-1:
    arr[i] = arr[i+1]  # this will left shift the elements
    i += 1
size -= 1

print(arr)
arr1 = []
for i in range(size):
    x = arr[i]
    # appending the elements upto size bcz extra copied ele will be there
    arr1.append(x)
print("updated list after deletion", arr1)

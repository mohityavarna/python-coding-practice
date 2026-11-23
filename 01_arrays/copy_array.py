# copy a array but will be stored at same address
from numpy import *

arr1 = array([2, 6, 8, 1, 3])
arr2 = arr1
arr1[1] = 7
print(arr1)  # [2 6 8 1 3]
print(arr2)  # [2 6 8 1 3]
print(id(arr1))  # 2369716348816
print(id(arr2))  # 2369716348816


# shallow copy with view - makes differnt location but one array change can change the other one

arr3 = array([2, 6, 8, 1, 3])
arr4 = arr3.view()

arr3[1] = 7

print(arr3)  # [2 7 8 1 3]
print(arr4)  # [2 7 8 1 3]
print(id(arr3))  # 2066066270000
print(id(arr4))  # 2066066270096

# deep copy but this time one array change cannot be seen in another array

arr5 = array([2, 6, 8, 1, 3])
arr6 = arr5.copy()

arr5[1] = 7

print(arr5)  # [2 7 8 1 3]
print(arr6)  # [2 6 8 1 3]
print(id(arr5))
print(id(arr6))

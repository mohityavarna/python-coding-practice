# Installing numpy for 2-d arrays
# pip - pip install packages
# go to cmd - pip3 install numpy


from numpy import *

arr = array([1, 2, 35, 67])
print(arr)

arr1 = linspace(0, 15, 16)  # it will divide 0 to 15 into 16 parts
print(arr1)

arr2 = linspace(0, 15)  # dont mention step then it will bydefault 50 parts

arr3 = arange(1, 15, 2)
print(arr3)

arr4 = logspace(1, 40, 5)  # in the of 10 ^a and 10^b
print(arr4)

arr5 = ones(5)  # array of 5 ones
print(arr5)

arr6 = zeros(5)  # array of 5 zeros
print(arr6)

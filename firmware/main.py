import numpy as np

from ConvertToSTL import ConvertToSTL

to = ConvertToSTL("fileok")
print(to.verifytest())

originalFile = input("Enter your file path: ")
numbers = np.fromfile(originalFile, dtype=np.uint8)

print("Total numbers in file:", numbers.size)

np.set_printoptions(threshold=np.inf)
print(numbers)
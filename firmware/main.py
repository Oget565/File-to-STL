import numpy as np

from ConvertToSTL import ConvertToSTL

buildplate = 225, 225 #width * lenght

originalFile = input("Enter your file path: ")

to = ConvertToSTL(originalFile, buildplate)
to.converttostl()

#numbers = np.fromfile(originalFile, dtype=np.uint8)
#print("Total numbers in file:", numbers.size)
#np.set_printoptions(threshold=np.inf)
#print(numbers)
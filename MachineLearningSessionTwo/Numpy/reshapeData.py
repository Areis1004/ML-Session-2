import numpy as np

salaryArray = np.array([1, 2, 3, 4, 5, 6, 7, 8,9 ,10, 11, 12]) 

salaryArray = salaryArray.reshape(-1, 1)

print(salaryArray)

print(salaryArray.shape)
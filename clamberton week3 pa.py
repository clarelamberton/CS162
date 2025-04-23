import numpy as np

array = np.random.randint(0,15, size=(5,5), dtype=int)
print(array)
#printing the 5x5 array
print(f"row {array[1,2]}")
print(f"sum of all elements in the array {np.sum(array)}")
print(f"the mean of each row {np.mean(array, axis=1)}")
print(f"the maximum of each row {np.max(array, axis=1)}")


import numpy as np
# Assuming `array` is a numpy array and `my_list` is a Python list
array = np.array([1, 2, 3])
my_list = [1, 2, 3]

# Element-wise comparison
list_equals_array = all(x == y for x, y in zip(my_list, array))
print("List equals array:", list_equals_array)

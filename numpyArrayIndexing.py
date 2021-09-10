import numpy as np
arr = np.arange(0, 11)
print(arr[3])
print(arr[0:5])
print(arr)
print(arr[5:]) #Everything beyond index 5
print(arr[:8]) #Everything before index 8
slice_of_arr = arr[0:6]
print(slice_of_arr)
slice_of_arr[:] = 99 #Gonna change the elements in arr too
print(arr)
arr_copy = arr.copy()
print(arr_copy)
arr_copy[:] = 100 #original array will not be affected
print(arr_copy)
print(arr)

# 2d arrays
arr_2d = np.array([[5,10,2],[20, 25, 3], [35, 40, 3]])
print(arr_2d)
print(arr_2d[0][1])
print(arr_2d[0,1])
print(arr_2d[:2,1:])
print(arr_2d[:2])

print(arr)
print(arr > 5)
print(arr < 10)
print(arr[arr<10])
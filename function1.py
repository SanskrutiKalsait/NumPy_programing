
# import numpy as np
# arr = np.zeros(3)
# print(arr)
# print(arr.dtype)

# import numpy as np
# arr1=np.zeros(3,dtype=int)
# print(arr1)
# print(arr1.dtype)

# import numpy as np
# arr = np.ones(3)
# print(arr)
# print("1d array data type :",arr.dtype)

# # arr1=np.ones(3,dtype=int)
# # print(arr1)
# # print(arr1.dtype)

# import numpy as np
# arr = np.zeros(3,4,dtype=int)
# print(arr)
# print("2d array data type :", arr.dtype)


# import numpy as np

# arr = np.ones((2,5,6))
# print(arr)

# arry1 =np.ones((2,5,6),dtype=int)
# print(arry1)
# print("3d array data type :", arry1.dtype)


#eye
# import numpy as np
# ar =np.eye(3)
# print(ar)
# print(ar.dtype)


# import numpy as np
# arr=np.eye(3,5,dtype=int)
# print(arr)
# print(arr.dtype)

# #diag
# import numpy as np
# arr1 =np.diag([1,2,3,4,67,4,89,3,3])
# arr2 = np.unique(arr1)
# print(arr1)
# print(arr1)
# print("unique number:",arr2)
# print("count unique number:", arr2)


# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])

# # print(a.size)
# import numpy as np
# a = np.array([1, 2, 3])

# print(a.itemsize)

import numpy as np
arr = np.random.randint(1,10,5)
print("original array:",arr)
max = arr.max()
print("maximum value position",arr.argmin())
print("maximum :" ,max)







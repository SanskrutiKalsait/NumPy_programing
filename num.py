#create 2d array ,print original array ,check dimension of the og array,find unique elements,find cout of the elements,
# convert into 3d array,find uniqueness and unique element count ,print the dimension


import numpy as np

arr = np.array([[1,2,3,],[4,5,6],[7,8,9],[10,11,12]])
print("original array",arr)
print("dimension of original array:",arr.ndim)
ele = np.unique(arr)
print("count unique element",ele)
print(ele)
reshape = arr.reshape(1,4,3)
print(reshape)
print("dimension of original array:",reshape.ndim)

# print("____________________")

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print("original array :" , arr)
# slicing = arr[2:6].copy()
# slicing[:]=0
# print(slicing)
# print("original:", arr)

# print("____________________")

# import numpy as np
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("original array :" , arr)
# slicing = arr[0,0:3].copy()
# slicing[:]=0
# print(slicing)
# print("original:", arr)

# print("____________________")

# import numpy as np
# arr = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print("original array :" , arr)
# slicing = arr[0,0,0:3].copy()
# slicing[:]=0
# print(slicing)
# print("original:", arr)


# a= [1,2,3,4,5,6,7,8,9,10,11,12]
# print(a[ :4])
# print(a[ : ])
# print(a[4:9])


# a =np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# print("A dimension :", a.ndim)
# x = a.reshape(2,6)
# print(x)
# print("x dimension:",x.ndim)

# import numpy as np
# a= np.array([10,20,30,40])
# print(a[0])
# print(a[1])
# print(a[2])

# import numpy as np
# a =np.array([1,2,3,4])
# print("a:", a.ndim)

# import numpy as np
# a = np.array([1,2,3,4,5,6,7,8,9])
# print(a[ :4])
# print(a[4:])
# print(a[ : ])

# import numpy as np
# a = np.array([10,20,30,40])
# b = np.array([40,50,60,70])
# result = a+b
# print(result)

# import numpy as np
# try:
#     a=np.array([10,20,30,40,])
#     b=np.array([50,60,70,80])
#     result= a+b
#     print(result)
# except(ValueError):
#     print("you have diffrence in the value provide for the array")


# # copy and view
# # Creates a new independent array containing the same data.

# # 1d array

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print("original array :" , arr)
# slicing = arr[2:6].copy()
# slicing[:]=0
# print(slicing)
# print("original:", arr)

# #2d array

# import numpy as np
# arr = np.array([[1,2,3,4,5,6,7,8,9,10,11,12]])
# print("original array :" , arr)
# slicing = arr[0,0:6].copy()
# slicing[:]=0
# print(slicing)
# print("original:", arr)

# #3d array

# import numpy as np
# arr = np.array([[[1,2,3,4,5,6,7,8,9,10,11,12]]])
# print("original array :" , arr)
# slicing = arr[0,0,0:6].copy()
# slicing[:]=0
# print(slicing)
# print("original:", arr)


# import numpy as np

# arr = np.array([[1,2,3,],[4,5,6],[7,8,9],[10,11,12]])
# print("original array:",arr)
# print("dimension of original array:",arr.ndim)
# ele = np.unique(arr).size

# print("count unique element:",ele)
# reshape = arr.reshape(1,4,3)
# print(reshape)
# print("dimension of original array:",reshape.ndim)
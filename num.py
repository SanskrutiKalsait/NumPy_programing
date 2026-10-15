# #create 2d array ,print original array ,check dimension of the og array,find unique elements,find cout of the elements,
# # convert into 3d array,find uniqueness and unique element count ,print the dimension


# import numpy as np

# arr = np.array([[1,2,3,],[4,5,6],[7,8,9],[10,11,12]])
# print("original array",arr)
# print("dimension of original array:",arr.ndim)
# ele = np.unique(arr)
# print("count unique element",ele)
# print(ele)
# reshape = arr.reshape(1,4,3)
# print(reshape)
# print("dimension of original array:",reshape.ndim)

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
# # print("original:", arr)

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


# import numpy as np

# arr = np.array([10, 25, 7, 42, 18])


# largest = np.max(arr)
# print(largest)



        #numpay#
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# print(arr)

# #1D array

# ar = np.array([10,20,30,40,50])
# print("1D array:",ar)

# #2 D array
# a = np.array([[1,2,3,4,],[5,6,7,8]])
# print("2D array:",a)

# # 3D array
# a = np.array([[[1,2,3,4,],[5,6,7,8],[9,10,11,12]]])
# print("3D array:",a)

#ndim
# a = np.array([[1,2,3,4,],[5,6,7,8]])
# print(a)
# print("dimestion of a:", a.ndim)

#find unique number
# num = np.array([1,2,3,4,5,6,6,66,7,77,7])
# print("original array",num)
# print("dimension of original array:",num.ndim)
# org = np.unique(num)
# print("count unique element",org.size)
# print(org)

#shape
# number = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("shape:",number.shape)

# #reshape
# numb = np.array([1,2,3,4,5,6,7,8,9])
# print(numb)
# reshape = numb.reshape(1,3,3)
# print("reshape:",reshape)


# #resize
# n= np.array([1,2,3,4,5,6,7,8,9])
# new = np.resize(n,(3,4))
# print(new)

# #dtype
# n= np.array([1,2,3,4,5,6,7,8,9])
# print(n.dtype)

# #zeros 1D
# arr = np.zeros(3)
# print(arr)
# print(arr.dtype)

# arr1 =np.zeros(3,dtype=int)
# print(arr1)
# print(arr1.dtype)

# # zeros 2D array 
# ar =np.zeros((4,3))
# print(ar)
# print(ar.dtype)

# ar1 =np.zeros((4,3),dtype=int)
# print(ar1)
# print(ar1.dtype)

# # zeros 3D array 
# ar =np.zeros((1,4,3))
# print(ar)
# print(ar.dtype)

# ar1 =np.zeros((1,4,3),dtype=int)
# print(ar1)
# print(ar1.dtype)

# ##eye 
# arr = np.eye(3,dtype=int)
# print(arr)

# #dig
# arr = np.diag([1,2,3,4,5])
# print(arr)

# #random.randint
# arr = np.random.randint(1,10,3)
# print(arr)

# #random .rand()
# arr = np.random.rand(5,3)
# print(arr)

# #ranom .randn()
# arr = np.random.randn(3)
# print(arr)

# #sqrt 
# a =np.array([1,2,3,4,5,6])
# print("original array:",a)
# ar =np.sqrt(a)
# print("sqrt value:",ar)

# #sin
# sinn =np.sin(a)
# print("sin value:",sinn)

# #cos
# coss =np.cos(a)
# print("cos value:",coss)

# #linespace
# license= np.linspace(1,2,3)
# print(license)

# #conditional statements
# arr =np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
# a = arr>10
# print(a)
# print(arr[a])

# #and 
# ar = arr[(arr>4)&(arr<14)]
# print(ar)

# #or
# arrr =arr
# #and 
# ar = arr[(arr>4)|(arr<14)]
# print(ar)

# #stacking
#1 horizontal
# import numpy as np
# a =np.array([1,2,3,4])
# b =np.array([5,6,7,8])
# c =np.hstack((a,b))
# print("horizantal :",c)

# # 2 vertical
# a =np.array([1,2,3,4])
# b =np.array([5,6,7,8])
# c =np.vstack((a,b))
# print("vertical :",c)


# #copy and view
# arr = np.array([1, 2, 3])
# new_arr = arr.copy()
# new_arr[0] = 100
# print(arr)
# print(new_arr)


# arr = np.array([1, 2, 3])
# new_arr = arr.view()
# new_arr[1] = 40
# print(arr)
# print(new_arr)


# import numpy as np

# arr = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# app = arr.flatten()
# app[0:]=0
# print("origiinal array:",arr)
# print("flatten array:",app)

# arr = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# app = arr.ravel()
# app[0:]=0
# print("origiinal array:",arr)
# print("flatten array:",app)

# arr = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# # a = arr.transpose()
# # print(np.transpose(arr))
# print(arr.T)

# arr = np.array([1,2,3,4])
# a = np.expand_dims(arr,axis=0)
# print(a.shape)
# print("zeros:",a)

# arr = np.array([1,2,3,4])
# a = np.expand_dims(arr,axis=1)
# print(a.shape)
# print("ones;",a)

# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# a =np.expand_dims(arr,axis=0)
# print(a.shape)
# print("ones:",a)

# arrr =np.array([2,3,4,5,6,7,8])
# b = np.expand_dims(arrr,axis=0)
# print(a.shape)
# print("zeros:",b)

# arr = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# app = arr.ravel()
# # app[0:]=0
# # print("origiinal array:",arr)
# # print("flatten array:",app)

import numpy as np
# # arr = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# # app = arr.ravel()
# # app[0:]=0
# # print("original array:",arr)
# # print("reval array:",app)

arrr= np.array([[34,56,77,54],[45,67,23,44]])
appp = arrr.flatten()
appp[0:]=0
print("original array:",arrr)
print("flatten array:",appp)


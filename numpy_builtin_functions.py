import numpy as np

print("Creating Numpy array using np.zeros() function that takes size as input")

x = np.zeros((3,4))

#default data type is float

print("The Numpy Array is:\n",x)
print("Number of Dimensions : ",x.ndim)
print("Shape : ",x.shape)
print("Size : ",x.size)
print("Data Type of elements is :",x.dtype)
print("Data Type of the object is : ",type(x))
#np.save("my_array_with_numpy",arr)

print()

print("Creating Numpy array using np.ones() function that takes size as input")

y = np.ones((5,4),dtype = None)
#default data type is float

print("The Numpy Array is :\n",y)
print("Number of Dimensions : ",y.ndim)
print("Shape : ",y.shape)
print("Size : ",y.size)
print("Data Type of elements is :",y.dtype)
print("Data Type of the object is : ",type(y))

print()

print("Creating Numpy array using np.full() function that takes size and constant as input")

z = np.full((6,5),4,dtype = None)
#default data type is int

print("The Numpy Array is :\n",z)
print("Number of Dimensions : ",z.ndim)
print("Shape : ",z.shape)
print("Size : ",z.size)
print("Data Type of elements is :",z.dtype)
print("Data Type of the object is : ",type(z))

"""
np.eye(N)
this function takes a N as input and returns a N*N Matrix
default is float
"""
print()

print("Creating Numpy array using np.eye() function that takes N as input")

a = np.eye(8,dtype=None)
#default data type is float

print("The Numpy Array is :\n",a)
print("Number of Dimensions : ",a.ndim)
print("Shape : ",a.shape)
print("Size : ",a.size)
print("Data Type of elements is :",a.dtype)
print("Data Type of the object is : ",type(a))

print()

print("Creating Numpy Array using np.diag() that takes diagonal elements as input object")

b = np.diag((1,2,3,4,5))
#default dtype is int

print("The Numpy Array is :\n",b)
print("Number of Dimensions : ",b.ndim)
print("Shape : ",b.shape)
print("Size : ",b.size)
print("Data Type of elements is :",b.dtype)
print("Data Type of the object is : ",type(b))

print()

print("Creating Numpy Array using np.arange() that generate elements from START:STOP:STEP(Stop  Exclusive) ")

c = np.arange(50,500,50,dtype = None)
#default dtype is int
#upper bound exclusive
#returns evenly spaced values within a given interval

print("The Numpy Array is :\n",c)
print("Number of Dimensions : ",c.ndim)
print("Shape : ",c.shape)
print("Size : ",c.size)
print("Data Type of elements is :",c.dtype)
print("Data Type of the object is : ",type(c))

print()

print("Creating Numpy Array using np.linspace() that generate elements from START:STOP:N:(Float Values) ")

d = np.linspace(50,500,100,dtype = None, endpoint= None)
#default dtype is float
#upper bound inclusive and can be stopped with endpoint = False
#returns evenly spaced values within a given interval


print("The Numpy Array is :\n",d)
print("Number of Dimensions : ",d.ndim)
print("Shape : ",d.shape)
print("Size : ",d.size)
print("Data Type of elements is :",d.dtype)
print("Data Type of the object is : ",type(d))

print()

print("Creating Numpy Array using np.reshape() that reshapes nparray if original and specified shapes are valid ")

e = np.arange(25)
f = np.reshape(e,(5,5))
#default dtype is float
#upper bound inclusive and can be stopped with endpoint = False
#returns evenly spaced values within a given interval

print("1d Array is :\n",e)
print("Reshaped Array : \n",f)
print("Number of Dimensions : ",f.ndim)
print("Shape : ",f.shape)
print("Size : ",f.size)
print("Data Type of elements is :",f.dtype)
print("Data Type of the object is : ",type(f))

print()

print("Creating Numpy Array using np.reshape METHOD that reshapes nparray if original and specified shapes are valid ")

"""
reshape is also a method that transforms nparray to specified size.
This allows us to create and reshape nparrays in one line of code.
"""

g = np.arange(25).reshape(5,5)

#default dtype is float
#upper bound inclusive and can be stopped with endpoint = False
#returns evenly spaced values within a given interval

print("Numpy Array : \n",g)
print("Number of Dimensions : ",g.ndim)
print("Shape : ",g.shape)
print("Size : ",g.size)
print("Data Type of elements is :",g.dtype)
print("Data Type of the object is : ",type(g))

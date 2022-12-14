import numpy as np

print("Creating Numpy array using np.random.random() function that takes size as input")

"""
first random refers to random module in numpy and
second random refers to the actual function

This function creates the  matrix with values ranging from 0 to 1(exclusive)
with a specified shape
"""

x = np.random.random((3,4))

#default data type is float
#doesnot accept any dtype argument (if specified - throws an error)

print("The Numpy Array is:\n",x)
print("Number of Dimensions : ",x.ndim)
print("Shape : ",x.shape)
print("Size : ",x.size)
print("Data Type of elements is :",x.dtype)
print("Data Type of the object is : ",type(x))


print()

print("Creating Numpy array using np.random.randint(START,STOP,SIZE=(shape))")

"""
random refers to random module in numpy and
randint refers to the actual function

This function creates the  matrix with values ranging from START to STOP(exclusive)
with a specified shape
"""

y = np.random.randint(5,50,size=(3,4))

#default data type is int
#as the randint() name suggests - it gives only integers
#it accepts dtype argument  but throws an error if float is passed.

print("The Numpy Array is:\n",y)
print("Number of Dimensions : ",y.ndim)
print("Shape : ",y.shape)
print("Size : ",y.size)
print("Data Type of elements is :",y.dtype)
print("Data Type of the object is : ",type(y))

print()

print("Creating Numpy array using np.random.normal(MEAN,STANDARD DEVIATION,SIZE=(Shape)) function")

"""
random refers to random module in numpy and
normal refers to the actual function

This function creates the  matrix with values that have the specified mean and
standard deviation
with a specified shape
"""

x = np.random.normal(0,0.1,(3,3))

#default data type is float
#doesnot accept any dtype argument (if specified - throws an error)

print("The Numpy Array is:\n",x)
print("Number of Dimensions : ",x.ndim)
print("Shape : ",x.shape)
print("Size : ",x.size)
print("Data Type of elements is :",x.dtype)
print("Data Type of the object is : ",type(x))

print('The elements in X have a mean of:', x.mean())
print('The maximum value in X is:', x.max())
print('The minimum value in X is:', x.min())
print('Y has', (x < 0).sum(), 'negative numbers')
print('Y has', (x > 0).sum(), 'positive numbers')


print()

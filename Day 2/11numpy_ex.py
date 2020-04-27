import numpy as np

a = np.array([]) # ([1,2,3]), ([[]]), ([[1,2],[3,4]])
print("-----------------------------------------------")
print (a)
b = np.arange(10)
print("-----------------------------------------------")
print (b)
c = b.reshape(2,5)
print("-----------------------------------------------")
print(c)
d = np.linspace(3,10,6) # try 9, 10 ...
print("-----------------------------------------------")
print(d)
e = np.random.randint(1000,size = (4,5))
print("-----------------------------------------------")
print(e)
f = np.empty((2,2))
print("-----------------------------------------------")
print(f)
g = np.ones((4,5))
print("-----------------------------------------------")
print(g)
h = np.zeros((3,5))
print("-----------------------------------------------")
print(h)
print("-----------------------------------------------")


Slicing

arr = np.arange(10)
print (arr)
print("-----------------------------------------------")
print(arr[3:7])     # 3 to 6 (exclude 7)
print(arr[:5])      # start to 4 (exclude 5)
print(arr[4:])      # 4 to end
print(arr[2:7:2])   # 2 to 6 with each as a step of 2 (exclude 7)
print(arr[:-1])     # start to index -2 (exclude -1)
print("-----------------------------------------------")

# 2D Slicing
arr2 = np.arange(20).reshape(4,5)
print("-----------------------------------------------")
print(arr2)
print(arr2[:,:])
print(arr2[1:3,3:4])
print(arr2[1:3,2:])
print("-----------------------------------------------")

# hstack and vstack
print("-----------------------------------------------")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.hstack((a,b))
print(c)
print("-----------------------------------------------")
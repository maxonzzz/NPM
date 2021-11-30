import numpy as np
import random
#TASK1
a = np.matrix([[ 1, 1 , 1], [0, 1, 1], [0, 0 , 1]])

b = np.matrix([[ 7, 5 , 3], [0, 7, 5], [0, 0 , 7]])

c = a * b
j = b * a
r = c - j
print("Task 1 = ")
print(r)

print("------------------------------------------------------------------")
#TASK2
task2 = np.matrix([[ -1, 0 , 2], [0, 1, 0], [1, 2 , -1]])
print("Task 2 = ")
print(np.linalg.matrix_power(task2, 2))

#TASK3
matrix1  = np.matrix([[ 5, 0 , 2, 3], [4, 1, 5, 3], [3, 1 , -1, 2]])
matrix2 = np.matrix([[6], [-2], [7], [4]])
task3 = matrix1 * matrix2

print('-----------------------------------------------')
print("Taks 3 = ")
print(task3)

#TASK4
matrix3 = np.matrix([[2, 3, 4], [1, 0, 6], [7, 8, 9]])
print('-----------------------------------------------')
print("Task 4 = ")
print(np.linalg.det(matrix3))
#TASK5
matrix5 = np.matrix([[1, 2, 3, 4], [-2, -1, -4, 3], [3, -4, -1, 2], [4, 3, -2, -1]])
print('-----------------------------------------------')
print("Task 5 = ")
print(np.linalg.det(matrix5))

#TASK6
matrix6 = np.matrix([[2, 1, 0, 0], [3, 2, 0, 0], [1, 1, 3, 4], [2, -1, 2, 3]])
print("----------------------------------------------")
print("Task 6 = ")
print(np.linalg.inv(matrix6))

#TASK7
matrix7 = np.matrix([[1, -1, 3, 4], [0, -1, 2, 1], [1, 1, -1, 2], [2, 3, -5, 3]])
print("------------------------------------------------")
print("Task 7 = ")
print(np.linalg.matrix_rank(matrix7))


#TASK8
matrix8 = np.matrix([[14, 4, 6], [5, -3, 2], [10, -11, 5]])
matrixv1 = np.matrix([[30], [15], [36]])
matrixa1 = np.matrix([[30, 4, 6], [15, -3, 2], [36, -11, 5]])
matrixb1 = np.matrix([[14, 30, 6], [5, 15, 2], [10, 36, 5]])
matrixz1 = np.matrix([[14, 4, 30], [5, -3, 15], [10, -11, 36]])
a2 = np.linalg.det(matrixa1)
b2 = np.linalg.det(matrixb1)
z2 = np.linalg.det(matrixz1)
x8 = np.linalg.det(matrix8)
if x8 != 0:
    x = a2/ x8  
    y = b2/ x8
    z = z2/ x8
print("-------------------------------------------")
print("Task 8 = ")
print("x =" ,x,"y = ", y,"z = ", z)
print("Revision = ")
print(np.linalg.solve(matrix8, matrixv1))



#TASK9
matrix10 = np.matrix([[1, 2, -1], [3, 4, 1], [5, 1, -3]])
matrixr2 = np.matrix([[-3], [1], [-2]])
j6 =  np.linalg.inv(matrix10)   
result = j6 * matrixr2
print("------------------------------")
print("Task 9 = ")
print(result)
print("revision = ")
print(np.linalg.solve(matrix10, matrixr2))

#TASK 10
print("---------------------------------------------------------------")
nrows = 10
ncols = 8
a = np.random.randint(100, size=(nrows,ncols))
print(" Element sum in str = " , a.sum(axis=1)) 

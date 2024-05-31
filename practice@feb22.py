#factorial using recursion
# def Factorial(val):

#     if val>1:
#         return val*Factorial(val-1)
#     else:
#         return 1


# value =int(input('enter the number:'))
# fact = Factorial(value)
# print('the factiorial of {} is {}'.format(value,fact))

# sum of first n numbers using recursion
# def SumOf(number):
#     if number >1:
#         return (number)+SumOf(number-1)
#     else:
#         return 1
# value = int(input('enter the range:'))
# Sum = SumOf(value)

# print('the sum of fist {} numbers is {}'.format(value,Sum))

#power of a number  using recursion


# def PowerOfNumber(power,val):
#     if power==0:
#         return 1
    
#     return val*PowerOfNumber(power-1, val)

# print('enter the number and the power')
# value,power = input().split()
# value = int(value)
# power = int(power)
# result = PowerOfNumber(power,value)
# print(result)


# matrix = [[ 3*i+j for j in range(3)]for i in range(3)]  cols = 3 is this given program
# print(matrix[1][2])

# rows = int(input('enter rows:'))
# cols = int(input('enter columns:'))

# OneD = [int(x) for x in input().split()]
# print('the one dimensional matrix is {}'.format(OneD))
# TwoD = []
# for i in range(rows):
#     TwoD.append([])
#     for j in range(cols):
#         TwoD[i].append(OneD[cols*i+j])
# print(TwoD)
# newMatrix =[]
# for j in range(cols):
#     if j %2==0:
#         for i in range(rows):
#             value = TwoD[i][j]
#             newMatrix.append(value)
#     else:
#         i = rows-1
#         while i>=0:
#             value = TwoD[i][j]
#             newMatrix.append(value)
#             i -=1
# finalMatrix = []
# for i in range(rows):
#     finalMatrix.append([])
#     for j in range(cols):
#         finalMatrix[i].append(newMatrix[cols*i+j])
# print(finalMatrix)

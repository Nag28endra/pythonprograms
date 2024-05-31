"""
*
**
***
****
*****
program
"""
# n = int(input('Enter rows: '))
# for i in range(0,n+1):
#     for j in range(0,i):
#         print("*",end=" ")

#     print()

"""
*****
****
***
**
*
program
"""
# n= int(input('Enter rows: '))
# for i in range(0,n+1):
#     for j in range(i,n):
#         print("*",end=" ")

#     print()

"""
    *
   **
  ***
 ****
*****
program
"""
# n= int(input('Enter rows: '))
# for i in range(0,n+1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(0,i):
#         print("*",end=" ")

#     print()

"""
*****
 ****
  ***
   **
    *
program
"""
# n= int(input('Enter rows: '))
# for i in range(0,n+1):
#     for j in range(0,i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")

#     print()

# n= int(input('Enter rows: '))
# for i in range(0,n+1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(0,i-1):
#         print("*",end=" ")
#     for k in range(0,i):
#         print('*',end=' ')


#     print()

# n= int(input('Enter rows: '))
# for i in range(0,n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(0,i-1):
#         print("*",end=" ")
#     for k in range(0,i):
#         print('*',end=' ')
#     print()
# for i in range(0,n+1):
#     for j in range(0,i):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for k in range(i,n):
#         print('*',end=' ')


#     print()

# n=  int(input('enter rows: '))
# for i in range(0,n):
#     for j in range(0,i):
#         print('*',end=' ')
#     print()
# for i in range(0,n+1):
#     for j in range(i,n):
#         print('*',end=' ')
#     print()

# n=  int(input('enter rows: '))
# for i in range(0,n):
#     for j in range(i,n):
#         print(' ',end=' ')
#     for j in range(0,i):
#         print('*',end=" ")
#     print()
# for i in range(0,n+1):
#     for j in range(0,i):
#         print(' ',end=' ')

#     for j in range(i,n):
#         print('*',end=' ')
#     print()

names  = ['nagendra','mini','bablu']

if (name := (input('enter your name :'))) in names:
    print(f'hello {name} welcome back')

else:
    print('name not found')
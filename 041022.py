"""sqare pattern"""

# rows = int(input('enter the no of rows:'))
# for i in range(rows):
#     for j in range(rows):
#         print("*",end=" ")
#     print()

"""hollow square pattern"""

# rows = int(input())

# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if (i==1 or j==1 or i == rows or j== rows):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#Rhombus pattern

rows = int(input())
for i in  range(0,rows):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(0,rows):
        print("*",end=" ")
    print()
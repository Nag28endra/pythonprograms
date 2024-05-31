# hollow square pattern:

# rows = int(input('enter the number of rows:'))

# for row in range(1,rows+1):
#     for col in range(1,rows+1):
#         if(row ==1 or row == rows or col == 1 or col == rows):
#             print("*",end=" ")

#         else:
#             print(" ",end=" ")
#     print()

#parallelogram pattern:
rows = int(input('enter no of rows:'))
cols = int(input('enter no of columns:'))

for i in range(0,rows+1):
    for j in range(0,i+1):
        print(" ",end=" ")
    for k in range(0,cols+1):
        print("*",end=" ")
    print()

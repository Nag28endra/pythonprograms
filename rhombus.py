rows = int(input('enter no of rows:'))

for i in range(0,rows):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(0,rows):
        print("*",end=" ")
    print()
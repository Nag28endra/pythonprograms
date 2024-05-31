row = int(input('enter no of rows:'))
col = int(input('enter no of cols:'))

for i in range(1,row+1):
    for j in range(1,col+1):
        if (i == 1 or i==row or j ==1 or j ==col):
            print("*",end= " ")
        else:
            print(" ",end = " ")
    print()
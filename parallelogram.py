row = int(input('enter no of rows:'))
col = int(input('enter no of cols:'))

for i in range(0,row):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(0,col):
        print("*",end=" ")
    print()

# #counting distinct elements
# size = int(input('enter the values range:'))

# numbers = [int(input()) for i in range(size)]
# print(numbers)
# length = len(numbers)

# visited = [False for i in range(length)]
# count = 0
# for i in range(0,length):
#     if visited[i]==True:
#         continue
#     for j in range(i+1,length):
#         if(numbers[i]==numbers[j]):
#             visited[j]=True
#     count += 1
# print(count)

# rows,column = input("enter row and column size").split()
# for row in range(int(rows)):
#     for col in range(int(column)):
#         print('*',end=" ")
#     print()

# rows = int(input())
# for row in range(1,rows+1):
#     for col in range(1,rows+1):
#         if (row ==1 or row==rows or col == 1 or col == rows):
#             print('*',end=" ")
#         else:
#             print(" ",end=' ')
#     print()

# size = int(input('enter the size of the list'))
# number =[int(input()) for i in range(size)]
# length = len(number)

# visited = [False for i in range(length)]

# repeated_values = []
# for i in range(length):
    
#     if visited[i]==True:
#         continue
#     count = 0
#     for j in range(i+1,length):
#         if(number[i]==number[j]):
#             visited[j] == True
#             count +=1 
#     if count>0:
#         value = number[i]
#         repeated_values.append(value)
# print(repeated_values)

# pairs = input('enter the values with comma separated:')

# pair_lst = []

# for pair in pairs.split(','):
#     pair = pair.strip()
#     value = tuple(map(int,pair.split()))
#     pair_lst.append(value)
# print(pair_lst)

# eSet = set()

# for (x,y) in pair_lst:
#     eSet.add((x,y))

#     if (y,x) in eSet:
#         print((x,y))

# values = input('enter the values with comman separated:')

# pairs = []

# for pair in values.split(","):
#     pair = pair.strip()
#     value = tuple(map(int,pair.split()))
#     pairs.append(value)
# print(pairs)

Range = int(input('enter the range to print the prime numbers:'))
for i in range(Range):
    sqr = pow(i,2)
    if i>3 and (sqr-1)%24 == 0:
        print(i,end=" ")
    
        
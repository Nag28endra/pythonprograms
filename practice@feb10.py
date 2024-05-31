# reverse the order of array without using any methods
#______________________________________________________
# def reverse_method(List,Start,End):
#     while Start<End:
#         List[Start],List[End] = List[End],List[Start]
#         Start += 1
#         End -=1
#     print(f"the reverse list is {List}")

# length = int(input('enter list size:'))
# mylist =[]
# for i in range(length):
#     number = int(input(f"the {i} number :"))
#     mylist.append(number)
# print(f"the list is {mylist}")
# list_len = len(mylist)
# start = 0
# end = list_len-1
# reverse_method(mylist,start,end)

#printing a list with half ascending and half descending order
#_____________________________________________________________
# size = int(input('enter the size of the list:'))
# mylist = []
# for i in range(size):
#     number = int(input())
#     mylist.append(number)
# print('the list is :')
# print(mylist,end=" ")
# print()
# mylist.sort()
# length = len(mylist)
# i = 0
# j = length -1 
# firstHalf = []
# while i<length//2 :
#     number=mylist[i]
#     firstHalf.append(number)
#     i += 1
# secondHalf=[]
# while j>=length//2:
#     number = mylist[j]
#     secondHalf.append(number)
#     j -= 1
# firstHalf.extend(secondHalf)
# print(f'the final result:{firstHalf  } ')
#_____________________________________________________
#   SETS

# List = [1,2,3,5]
# myset = set(List)
# print("the set is {}".format(myset))

# myset.add(28)
# print('the edited set is {}'.format(myset))
# myset.update({12,2000})
# print('the edited set is {}'.format(myset))
# popped_item=myset.pop()
# print('the poped_item is {}'.format(popped_item))
# popped_item=myset.pop()
# print('the poped_item is {}'.format(popped_item))

# set1 = {1,2,3,4,5}
# set2 = {2,3,6,7,8}
# print(set1.union(set2))
# print('the set intersection is {}'.format(set1.intersection(set2)))
# print('the set difference is {}'.format(set1.difference(set2)))

# row = int(input())
# col = int(input())
# matrix =[[]]
# for i in range(0,row):
#     for j in range(0,col):
#         number = int(input())
#         matrix.append(number)

# for i in range(0,row):
#     for j in range(0,col):
#         print(matrix[i][j])
#     print()

# def read_matrix():
#     matrix = []
#     print("Enter the elements of 3x3 matrix: ")
#     for i in range(3):
#         row = []
#         for j in range(3):
#             row.append(int(input("Enter an element: ")))
#         matrix.append(row)
#     return matrix

# matrix = read_matrix()

# print("The matrix is: ")
# for row in matrix:
#     print(row)
#_________________________________________________________
# finding the frequency of the element in the given list

arr=[]
size = int(input('enter the array size:'))

for i in range(size):
    print('enter {} element'.format(i))
    number = int(input())
    arr.append(number)
print('the list is {}'.format(arr))  
length = len(arr)

visited = [False for i in range(length)]

for i in range(length):

    if visited[i] == True:
        continue
    count = 1
    for j in range(i+1,length,1):
        if arr[i]==arr[j]:
            visited[j] = True
            count += 1
    
    print(arr[i],count)

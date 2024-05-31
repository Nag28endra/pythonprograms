# def isPalindrome(value):
#     number = value
#     reverse =0
#     while (number!=0):
#         number = number%10
#         reverse =(reverse*10)+number
#         number //= 10
#     if (reverse == value):
#         return True
#     else:
#         return False

# def LargestPalindrome(arr,n):
#     currentMaximum = -1
#     for i in range(n):
#         if(arr[i]>currentMaximum and isPalindrome(arr[i])):
#             currentMaximum = arr[i]
             

#     return currentMaximum

# arr = [1,232,9090,121,464]
# length = len(arr)
# print('the largest palindrome is ',LargestPalindrome(arr,length))

# counting distinct elements from the array

# def count(List,n):
#     visited = [False for i in range(n)]
#     count_dis = 0
#     for i in range(n):
#         if (visited[i]==True):
#             continue
        
#         for j in range(i+1,n):
#             if(arr[i]==arr[j]):
#                 visited[j]=True
#         count_dis += 1
#     print(count_dis)

# arr = [10, 30, 40, 20, 10, 20, 50, 10]
# length = len(arr)
# count(arr,length)


#sets
# set1= {12,23,34,33,67}
# set2= {22,245,23,33,56,67}
# List = [12,22,34,55,66]
# set3 = set(List)
# print('the first set:{}\nthe second set:{}\n the third set: {}'.format(set1,set2,set3))

# set3.update([27,45,28])
# print('the union of set1 and set2:{}'.format(set1.union(set2)))
# print('the updated set3 is {}'.format(set3))

# set3.remove(55)
# print('the set3 is {}'.format(set3))
# print(set1.issubset(set2))

# set1 = frozenset({'nagendra','vamis','shashank','namratha','preeti'})

# try:
#     set1.add('keerthi')
# except AttributeError as e:
#     print(e)


with open('file.txt','w') as file:
    file.write('hello welcome to files\n')
    file.write('this is nagendra the python developer and ML engineer\n')
with open('file.txt','r') as file:
    data = file.read()
    print(data)
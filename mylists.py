# names = ['vamsi','hari','shashank','ansaar','dev das'] 
# print(f'the first name is {names[0].title()}')
# print(f'the second name is {names[1].title()}')
# print(f'the third name is {names[2].title()}')
# print(f'the fourth name is {names[3].title()}')
# print(f'the fifthe name is {names[4].title()}')

# #----->changing the elements in the list
# myList = ['spiderman','superman','flash','batman','ironman']# list of super heros
# print(myList) #printing the list
# # to change any element in the list just replace it using the index value
# myList[2] = 'thor'
# print(myList) # printing the list that is modified 

# #---->adding a new element to the list
# myList = ['spiderman','superman','flash','batman','ironman'] #list with super heros

# # inorder to add new element to the list we need to 'append' the new element to the list using the 'append' method
# myList.append('thor') # when we add a new element to the list it is appended at the end of the list
# print(myList)
# myList.append('hulk')
# print(myList)

# #------->inserting an element into the list at any index

# myList = ['spiderman','superman','flash','batman','ironman']
# # we can insert the new element at any index using the insert() method, by passing the index and the value to be inserted.

# myList.insert(0,'thor')
# myList.insert(2, 'hulk')
# print(myList)

# #-------->removing an element from the list using 'del' and pop() method
# myList = ['spiderman','superman','flash','batman','ironman']
# # we can remove an element from the list with help of 'del' statement when we know the index of that particular value.
# del myList[3] # batman will be removed from the list
# print(myList)

# # also we can remove the element using the pop() method but here the end element of the list is removed as the pop operation is meant for stack so it recognizes the end element of the list as the top of the stack.
# popped_value = myList.pop()
# print(myList) #iron man will be removed from the list
# print(f'the popped value is {popped_value}')

# #we can remove the element of specific index using pop() method by passing the index value
# myList.pop(2)
# print(myList)

# #---->removing the elements of the list using the remove() method
# myList = ['spiderman','superman','flash','batman','ironman']
# # we don't know the index value of certain element then we can remove that element just using the remove() method by passing the element
# myList.remove('flash')
# print(myList) # flash will be removed from the list.

#--------------------------------exercise-----------------------------------#

# guests = ['rahul','vikas','vamsi','mahesh','satya']
# print(f'{guests[0]} is invited to the party')
# print(f'{guests[1]} is invited to the party')
# print(f'{guests[2]} is invited to the party')
# print(f'{guests[3]} is invited to the party')
# print(f'{guests[4]} is invited to the party')
# print()
# print(f'{guests[-1]} is not available to the party')
# guests[-1] = 'Ansaar'
# print(f'{guests[-1]} is invited to the party')

# guests = ['rahul','vikas','vamsi','mahesh','satya']
# guests.insert(0, 'hari')
# guests.insert(2, 'dev das')
# guests.append('ansaar')
# print(f'{guests[0]} is invited to the party')
# print(f'{guests[1]} is invited to the party')
# print(f'{guests[2]} is invited to the party')
# print(f'{guests[3]} is invited to the party')
# print(f'{guests[4]} is invited to the party')
# print(f'{guests[5]} is invited to the party')
# print(f'{guests[6]} is invited to the party')
# print(f'{guests[7]} is invited to the party')
# print()
# print('sorry guys only two people are invited to the party')
# pperson1 = guests.pop()
# print(f'sorry {pperson1} you are not invited to the party')
# pperson2 = guests.pop()
# print(f'sorry {pperson2} you are not invited to the party')
# pperson3 = guests.pop()
# print(f'sorry {pperson3} you are not invited to the party')
# pperson4 = guests.pop()
# print(f'sorry {pperson4} you are not invited to the party')
# pperson5 = guests.pop()
# print(f'sorry {pperson5} you are not invited to the party')
# pperson6 = guests.pop()
# print(f'sorry {pperson6} you are not invited to the party')

# print(guests)
# del guests

# print(guests)

# #----------->sorting the list using the sort() method
# myList = ['vamsi','hari','nagendra','ansaar','shashank','dev das']
# myList.sort()
# print(myList) # this prints the list elements in the sorted order

# myList.sort(reverse=True)
# print(myList) # this prints the list elements in the reverse sorted order.


# #---------->sorting the list elements without disturbing the original order using the sorted() method.
# myList = ['vamsi','hari','nagendra','ansaar','shashank','dev das']
# print('the original list is :')
# print(myList)
# print()
# print('the sorted list is :')
# print(sorted(myList)) # the sorted() method will not permanently sort the list elements.
# print()
# print('the original list again is :')
# print(myList)

# #--------> printing a list in reverse order without using sort(reverse = True).
# myList = ['vamsi','hari','nagendra','ansaar','shashank','dev das']
# myList.reverse() # here the reverse() method will not sort the elements in the reverse order. It just displays the original order of the list in the reverse order.
# print(myList)
# print(myList)
# print()
# myList.reverse()
# print(myList)
# print(f'the length of the list is :{len(myList)}')
 

# #------------------------exercise----------------------
# places = ['london','delhi','benguluru','australia','los angeles']
# print('the original list is :')
# print(places)
# print()
# print('the sorted list is:')
# print(sorted(places))
# print()
# print('the original list again is:')
# print(places)
# print()
# places.reverse()
# print('the reverse order of the list is:')
# print(places)
# print()
# print('the list back to its original order is:')
# places.reverse()
# print(places)
# places.sort()
# print()
# print('the sorted list is:')
# print(places)
# print()
# print('the sorted list in reverse order is:')
# places.sort(reverse=True)
# print(places)

# using 'for' loop to print the  elements in the list:
# names = ['vamsi','hari','shashank','ansaar','dev das']

# for name in names: #here is the name is a variable just like i we use.
#     print(name)

# for i in range(1,10):
#     print(i)

numbers = list(range(1,11))
print(numbers)








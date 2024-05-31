# #removing the duplicates from the list 
# myList = ['goku','vegeta','jiren','xeno goku','beerus','goku']
# print(list(dict.fromkeys(myList))) 
# # we can also use set() method to remove duplicates

# def myFilter(value):
#     if value>20:
#         return value

# if __name__ == "__main__":
#     myList= [12,23,11,56,98,10]
#     filteredList = list(filter(myFilter,myList))
#     print('the filtered list is {0}'.format(filteredList))

# def mapping(value):
#     return value**2

# if __name__ == "__main__":
#     myList= [12,23,11,56,98,10]
#     Alist = list(map(mapping,myList))
#     print(Alist)

# list_1 = ['goku','vegeta','gohan']
# list_2 = ['gohan','trunks','pan']
# list_3 = ['goten','bula','jiren']
# print(tuple(zip(list_1,list_2,list_3)))

# myList = [1,12,45,32,767,23,34,546,73,12,656,11,34,56,32,645,12,12,32]
# frequent = max(set(myList),key=myList.count)
# print(frequent)
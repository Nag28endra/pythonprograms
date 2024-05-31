# # SETS
# '''sets are unordered data types or data strucuters.
#     They won't allow duplicates.
    
#     Representation: <var> = {value1,value2,value3...}
# '''

# # creating a set using set() method
# myDictionary = ['alska','Madagascar','hambontota']
# print(set(myDictionary))


set1 = {1,2,3,4}
set2 = {4,6,7,3}

# set1.update(set2)
# print(set1)
print(set1.intersection(set2))
set1.intersection_update([4,6])
print(set1)


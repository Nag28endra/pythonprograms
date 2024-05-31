# string = "#"
# mylist = ["hello","world"]
# print(string.join(mylist))


# mylist = ['venkat','wants','to','live','with his friends']
# sentence =  " ".join(mylist)
# print(sentence)

# numbers = [1,2,3,4,5]
# mystring = ",".join(map(str,numbers))
# print(mystring)

# dictionary = {'name':'nagendra','branch':'cse'}
# details = "\n".join("{}:{}".format(k,v) for k,v in dictionary.items())
# print(details)

# dictionary = {'name':'nagendra','branch':'cse','fav_lang':'python'}
# details = list(dictionary.items())
# print(details)

# mylist = [('name', 'nagendra'), ('branch', 'cse'), ('fav_lang', 'python')]
# dictionary = dict(mylist)
# print(dictionary)

numbers = [12,22,12,523,1234,123,512,55]
def is_even(n):
    if n%2==0:
        return n
even_numbers = list(filter(is_even, numbers))
print(even_numbers)
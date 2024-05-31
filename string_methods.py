# some other methods that are associated with strings:
"""
----->len(): to find the length of the string
----->count(): to find how many times a value has occured.
----->find(): finds the index value if desired string or a value
----->index(): finds the first occurrance of the string.
----->split(): splits the string into list.
----->strip(): removes the unnecessary spaces in the string.
----->casefold(): converts the string to lower cases.
----->replace(): replaces the strings with another values.
----->list(): converts the string into the list 
----->reversed(): reverses the string.
----->bool(): gives the boolean values.
"""
# use of len()

# string = 'hello time travelers\n'
# length = len(string) #\n \t
# print(length)

#use of count()
# string = 'hello time travelers, now you guys are time travelling'
# print(f'the word "time" has occurred {string.count("time")} times') #var_name.count('value')

#use of find()
# string = 'hello time travelers, now you guys are time travelling'
# print(f'the word "time" as starting index at {string.find("time")}')

#use of index()
# string = 'hello time travelers, now you guys are time travelling'
# print(string.index('time'))

#use of split()
msg = 'time travelers'
print(msg.split()) #var_name.split()

# # use of strip()
# string = ' hello time travelers '
# print(f'the length of the actual string is {len(string)}')

# str = string.strip() #rstrip() lstrip()
# print(f'the length of the string after stripping is {len(str)}')

#use of casefold()
# string = 'Hello Time Travelers'
# print(string.casefold()) # it works similar to lower()

#use of replace()
# msg = 'hello welcome to python programming'
# print(msg.replace("programming", "course"))

#use of list()
# msg = 'hello welcome to python programming' #['hello','welcome'..]
# print(list(msg)) # msg.list() list(msg)

#use of reversed()
# msg = 'hello'
# print(list(reversed(msg)))

# use bool()

# var = 0
# print(bool(var))


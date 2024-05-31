# finding the length of the string without using the len () method

string = input('enter the string value:')
count = 0
for i in string:
    count +=1
print(f'the length of the string is {count}')
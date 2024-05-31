string = input('enter any value:')
count_words = len(string.split())
print(f'number of words inthe given string are {count_words}')

count = 0
for i in string:
    if i == ' ':
        count +=1
print(f'the number of words in the given string using for loop are: {count+1}')
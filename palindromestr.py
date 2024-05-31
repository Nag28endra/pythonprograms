string = input('enter the value:')
value = string.casefold()

rev_value = reversed(value)

if list(value) == list(rev_value):
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")
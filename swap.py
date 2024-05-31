# swapping two numbers using python code.

# num1 = int(input('enter the first number:'))
# num2 = int(input('enter the second number:'))

# print(f'the value num1 = {num1} and num2 = {num2}')

# temp = num1
# num1 = num2
# num2 = temp

# print(f'after swapping the num1 ={num1} and num2 = {num2}')

#swapping the numbers without using the 3rd variable
num1 = int(input('enter the first number:'))
num2 = int(input('enter the second number:'))

print(f'the value num1 = {num1} and num2 = {num2}')

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f'after swapping the num1 ={num1} and num2 = {num2}')
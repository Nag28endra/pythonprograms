number = int(input('enter the number:'))
sum =0 
length = len(str(number))
temp = number

while number !=0:
    reminder = number%10
    sum += pow(reminder,length)
    number = number//10

if temp == sum:
    print('armstrong')
else:
    print('not armstrong')


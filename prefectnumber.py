number = int(input('enter the number to check for perfect or not:'))
divisors = []
for i in range(1,number):
    if number %i == 0:
        divisors.append(i)

Sum = 0
length = len(divisors)
for j in range(length):
    Sum += divisors[j]
if Sum == number:
    print('the number is perfect')
else :
    print('the number is not perfect')

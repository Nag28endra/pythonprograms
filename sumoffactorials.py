# this is the program to find the sum of factorials is 1!+2!+.....

range = int(input('enter the range to find the sum of factorials:'))

i=1
fact =1
sum = 0
while (i<=range):
    
    fact = fact *i
    sum = sum + fact
    i+=1
print(f'the sum of factorials of {range} elements is {sum}')
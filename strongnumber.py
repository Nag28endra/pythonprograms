number = int(input('enter the number:'))
temp = number
sum =0         
while number!=0:
    
    remainder = number%10
    i = 1
    fact = 1
    while i<=remainder:
        fact *= i
        i +=1
   
    sum += fact
    number //= 10
if temp == sum:
    print('the number is strong number')
else:
    print('the number is not a strong number')
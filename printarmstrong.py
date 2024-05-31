number = int(input('enter the range:'))
low,high = 2,number

for i in range(low,high+1):
    length = len(str(i))
    sum =0
    temp = i
    while i!=0:
        remainder = i % 10
        sum += remainder**length
        i //= 10
    if temp == sum:
        print(temp,end=" ")
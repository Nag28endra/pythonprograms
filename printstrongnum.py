value_range = int(input('enter the range to find the list of strong numbers:'))
for i in range(value_range+1):
    temp = i
    sum = 0
    while i!=0:
        remainder = i%10
        k = 1
        fact = 1
        while k<=remainder:
            fact *= k
            k += 1
        sum += fact
        i //= 10
    if sum == temp:
        print(temp,end=" ")
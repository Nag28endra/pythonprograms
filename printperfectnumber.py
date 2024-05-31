value_range = int(input('enter the range to print the list of perfect numbers:'))

for i in range(value_range+1):
    divisors = []
    for j in range(1,i):
        if i %j == 0:
            divisors.append(j)
    length = len(divisors)
    sum = 0
    for k in range(length):
        sum += divisors[k]
    if sum == i:
        print(i,end=" ")
#method-1

numbers = list(map(int,input('enter the numbers: ').split()))
hcf = 1
for i in range(1,min(numbers)):
    if numbers[0]%i == 0 and numbers[1]%i==0:
        hcf = i

print(hcf)
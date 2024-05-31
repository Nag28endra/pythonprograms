# PRINTING THE ARMSTRONG NUMBERS IN THE GIVEN RANGE
# Range = int(input('enter the range:'))
# low,high = 2,Range

# for i in range(low,high+1):
#     sum = 0 
#     length = len(str(i))
#     temp = i
#     while i!=0:
#         remainder = i % 10
#         sum += remainder**length
#         i //= 10
#     if temp == sum:
#         print(temp,end=" ")

#FIBONACCI SERIES: FINDING THE NTH TERM
# def Nfibonacci(value):
#     if value<2:
#         return value
#     fs = [0,1]
#     for i in range(1,value):
#         fs.append(fs[i]+fs[i-1])
#     return fs[value]
# Range = int(input('enter the range:'))
# print(Nfibonacci(Range-1))

#FIBONACCI SERIES USING RECURSION
def fibonacci(value):
    if value <= 1:
        return value
    else:
        return (fibonacci(value-1)+fibonacci(value-2))

Range = int(input('enter the range:'))
for i in range(Range):
    print(fibonacci(i),end=" ")
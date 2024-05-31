def fibbonacciSeries(value):
    if value <=1:
        return value
    else:
        return (fibbonacciSeries(value-1)+fibbonacciSeries(value-2))

Range = int(input('enter the range:'))


for i in range(Range):
    print(fibbonacciSeries(i),end=" ")


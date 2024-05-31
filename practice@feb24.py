def FibonacciSeries(n,fib={}):
    if n in fib:
        return fib[n]
    if n<=1:
        fib[n]= n

    else:
        fib[n] = FibonacciSeries(n-1,fib)+FibonacciSeries(n-2,fib)+FibonacciSeries(n-3,fib)
    return fib[n]


n = int(input('enter range:'))
series = [FibonacciSeries(i) for i in range(n)]
print('the nth value of the series is :{} '.format(series[n-1]))
print(" ".join(str(i) for i in series))

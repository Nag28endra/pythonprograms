def Nfibonacci(n):
    if n <2:
        return n
    fs = [0,1]
    for i in range(1,n):
        fs.append(fs[i]+fs[i-1])
    return fs[n]

value = int(input("enter the range:"))
print(f'the Nth value of the fibonnaci series is {Nfibonacci(value-1)}')

#fibonacci series

def fibonacci(value):
    if value<=1:
        return value

    else:
        return fibonacci(value-1)+fibonacci(value-2)

paramrange = int(input('enter the range'))
print(fibonacci(paramrange))
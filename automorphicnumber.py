number = int(input('enter the number to check whether it is automorphic or not:'))
square = pow(number,2)
mod = pow(10,len(str(number)))

if square % mod == number:
    print('the number is automorphic')
else:
    print('the number is not automorphic')
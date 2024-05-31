#binary to decimal

bin_num = int(input('enter the binary number:'))
dec_val = 0
base =1
k = bin_num

while bin_num>0:
    rem = bin_num%10
    dec_val = dec_val + rem*base
    bin_num //= 10
    base *=2
print(f'binary:{k}\ndecimal:{dec_val}')
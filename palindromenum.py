# writing a program to find the whether given number is palindrome or not.

number = int(input('enter the number'))
dup = number    #121
reverse = 0
while number>0:                         #1>0      
    rem = number%10                      # 1%10 = 1       
    reverse = (reverse*10)+rem             #(12*10)+1   =121
    number = number//10                    # 1//10 = 0
if reverse == dup:                  #number =0
    print('the number is palindrome')
else:
    print('the number is not palindrome')

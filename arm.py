number=int(input("enter the range"))
dup=number
num=number
digit=0
add=0
length=len(str(number))
def arm(number,length):
    for i in range(length):
        digit=number%10
        num=num//10
        add=add+pow(digit,length)  
    if(add==dup):
        print("armstrong")
    else:
        print("not armstrong")    
while(number!=0):
    number=number-1
    length=len(str(number))  
    arm(number,length)


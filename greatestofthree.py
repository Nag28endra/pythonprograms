
def myFun():
    print('select which method to solve:\n1.Ternary\n2.Iterative approach\n')
    choice = int(input())
    if choice == 1:
        ternaryFun()
    elif choice == 2:
        iterativeFun()

# using ternary operator to find the largest number among the three
def ternaryFun():
    num1 = input('enter first number:')
    num2 = input('enter second number:')
    num3 = input("enter third number:")

    max = num1 if num1>num2 else num2
    max = num3 if num3>max else max
    print(f'{max} is the largest number')


# using if and elif statements to find the largest among the three
def iterativeFun():
    num1 = input('enter first number:')
    num2 = input('enter second number:')
    num3 = input("enter third number:")

    if num1>num2 and num1>num3:
        print(f'{mum1} is largest')
    elif num2>num1 and num2>num3:
        print(f'{num2} is largest')
    else:
        print(f'{num3} is largest')

myFun() #main method to start the program

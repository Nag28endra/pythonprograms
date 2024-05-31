#BALANCED PARANTHESIS

def CheckBalanced(expr):
    def CheckPair (val1,val2):
        if  ((val1 == '(' and val2==')' )or (val1 == '{' and val2 == '}') or (val1=='[' and val2 == ']')):
            return True
            
    stack = []
    for i in range(len(expr)):
        if (expr[i]=='(' or expr[i]=='[' or expr[i] == '{'):
            stack.append(expr[i])
        else:
            if (len(stack)==0):
                return False
            elif CheckPair(stack[-1],expr[i]) :
                stack.pop()
                continue

            return False
    return True



expression = input('enter the expression:')

print(CheckBalanced(expression))
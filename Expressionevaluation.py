class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def isEmpty(self):
        return len(self.stack)==0

    def popitem(self):
        if self.isEmpty():
            print("STACK UNDERFLOW")
            return

        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("STACK UNDERFLOW")
            return
        else:
            return self.stack[-1]

def ExpressionEvaluation(expression):
    operatorStack = Stack()
    operandStack = Stack()

    precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}

    i = 0 
    while i<len(expression):

        if expression[i]==" ":
            i +=1
            continue
        elif expression[i]=="(":
            operatorStack.push('(')

        elif expression[i].isdigit():
            j = i
            while j<len(expression) and expression[j].isdigit():
                j +=1
            operandStack.push(int(expression[i:j]))
            i = j-1

        elif expression[i]==')':
            while operatorStack.peek()!='(':
                operator = operatorStack.popitem()
                operand1 = operandStack.popitem()
                operand2 = operandStack.popitem()
                result = expressionOperation(operator,operand1,operand2)
                operandStack.push(result)
            operatorStack.popitem()

        else:
            while not operatorStack.isEmpty() and precedence.get(operatorStack.peek(),0)>=precedence.get(expression[i],0):
                operator = operatorStack.popitem()
                operand1 = operandStack.popitem()
                operand2 = operandStack.popitem()
                result = expressionOperation(operator,operand1,operand2)
                operandStack.push(result)
            operatorStack.push(expression[i])

        i += 1
    while not operatorStack.isEmpty():
        operator = operatorStack.popitem()
        operand2 = operandStack.popitem()
        operand1 = operandStack.popitem()
        result = expressionOperation(operator,operand1,operand2)
        operandStack.push(result)
    
    # Return the final result
    return operandStack.popitem()

def expressionOperation(oper,val1,val2):
    if oper == '+':
        return val1+val2

    elif oper == '-':
        return val1-val2

    elif oper == '*':
        return val1*val2

    elif oper == '/':
        return val1//val2

    elif oper == '^':
        return val1**val2

expression = "(10+2*10)^2"
answer=ExpressionEvaluation(expression)
print(f'the expression evaluation of {expression} is {answer}')

        


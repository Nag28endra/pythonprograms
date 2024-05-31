class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def popitem(self):
        if self.isEmpty():
            print('STACK UNDERFLOW')
            return
        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print('STACK UNDERFLOW')
            return

        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack)==0

def infixtopostfix(expression):
    operatorStack = Stack()
    precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
    postfix = []

    i =0 
    while i<len(expression):
        if expression[i]==" ":
            i+=1
            continue
        elif expression[i]=='(':
            operatorStack.push('(')

        elif expression[i].isdigit():
            j = i
            while j<len(expression) and expression[j].isdigit():
                j +=1
            postfix.append(int(expression[i:j]))
            i = j-1

        elif expression[i]==')':
            while operatorStack.peek() !='(':
                postfix.append(operatorStack.popitem())
            operatorStack.popitem()

        else:
            while not operatorStack.isEmpty() and precedence.get(operatorStack.peek(),0)>=precedence.get(expression[i],0):
                postfix.append(operatorStack.popitem())
            operatorStack.push(expression[i])
        i +=1

    while not operatorStack.isEmpty():
        postfix.append(operatorStack.popitem())

    return ' '.join(str(x) for x in postfix)

expression = input('enter the expression:')
result = infixtopostfix(expression)

print(f'the infix to post fix notation of the expression {expression} is {result}')
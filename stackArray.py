class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack)==0

    def push(self,data):
        self.stack.append(data)
        return self.stack

    def popitem(self):
        if self.isEmpty():
            print('the stack is empty')
            return

        else:
            self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print('the stack is empty')
            return

        else:
            return self.stack[-1]

    def traverse(self):
        if self.isEmpty():
            print('the stack is empty')
            return

        else:
            print(' '.join([str(x) for x in self.stack]))

sObj = Stack()
sObj.push(12)
sObj.push(13)
sObj.push(14)

print('the stack is :')
sObj.traverse()

# sObj.popitem()
# print('the stack after the pop operation:')
# sObj.travers e()

print(f'the first element of the stack {sObj.peek()}')

        
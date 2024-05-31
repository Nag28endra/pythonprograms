class Stack:
    def __init__(self):
        self.stack = []
        self.reverse =[]

    def push(self,data):
        self.stack.append(data)

    def isEmpty(self):
        return len(self.stack)==0

    def pop(self):
        if self.isEmpty():
            None
        else:
            popped = self.stack.pop()
            self.reverse.append(popped)

    def printReverse(self):
        for i in range(len(self.stack)+1):
            self.pop()
        print('the reverse string:',end='')
        print(''.join(x for x in self.reverse))




def splitString(value):
    stringList = [x for x in value]
    for i in range(len(stringList)):
        s.push(stringList[i])
    # print(stringList)

    
s = Stack()
value = input('enter the string: ')
print(f'original string: {value}')
splitString(value)
s.printReverse()

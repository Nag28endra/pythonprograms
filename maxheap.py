class maxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self,val):
        self.heap.append(val)
        self.shiftUp(len(self.heap)-1)

    def shiftUp(self,index):
        parent_index = (index-1)//2
        if parent_index>=0 and self.heap[parent_index]<self.heap[index]:
            self.heap[parent_index],self.heap[index]=self.heap[index],self.heap[parent_index]
            self.shiftUp(parent_index)

    def extract(self):
        max_value = self.heap[0]
        end_value = self.heap.pop()
        if self.heap:
            self.heap[0] = end_value
            self.shiftDown(0)
        return max_value

    def shiftDown(self,index):
        left_child = 2*index +1
        right_child = 2*index +2
        large = index
        if left_child<len(self.heap) and self.heap[left_child]>self.heap[large]:
            large = left_child
        if right_child <len(self.heap) and self.heap[right_child]>self.heap[large]:
            large = right_child
        if large != index:
            self.heap[large],self.heap[index]=self.heap[index],self.heap[large]
            self.shiftDown(large)

    def getMax(self):
        return self.heap[0] if self.heap else None

    def display(self):
        for i in self.heap:
            print(i,end=' ')
        print()

mp = maxHeap()
mp.insert(28)
mp.insert(20)
mp.insert(50)
mp.insert(60)
mp.display()
print(mp.extract()) 
print(mp.getMax())     
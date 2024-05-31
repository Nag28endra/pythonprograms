class minHeap:
    def __init__(self):
        self.heap = []

    def insert(self,value):
        self.heap.append(value)
        self.shiftUp(len(self.heap)-1)

    def shiftUp(self,index):
        parent_index = (index-1)//2
        if parent_index>=0 and self.heap[parent_index]>self.heap[index]:
            self.heap[parent_index],self.heap[index]=self.heap[index],self.heap[parent_index]
            self.shiftUp(parent_index)
    
    def extract_min(self):
        min_value = self.heap[0]
        end = self.heap.pop()
        if self.heap:
            self.heap[0]=end
            self.shiftDown(0)
        return min_value

    def shiftDown(self,index):
        left_child = 2*index+1
        right_child = 2*index+2
        smallest  = index

        if left_child<len(self.heap) and self.heap[left_child]<self.heap[smallest]:
            smallest = left_child
        if right_child<len(self.heap) and self.heap[right_child]<self.heap[smallest]:
            smallest = right_child
        if smallest !=index:
            self.heap[smallest],self.heap[index]=self.heap[index],self.heap[smallest]
            self.shiftDown(smallest)
        
    def getMin(self):
        return self.heap[0] if self.heap else None

    def display(self):
        for i in self.heap:
            print(i,end=" ")
        print()

mip = minHeap()
mip.insert(45)
mip.insert(33)
mip.insert(29)
mip.insert(20)
mip.insert(42)
mip.display()
print(mip.extract_min())
print(mip.getMin())
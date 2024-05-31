class Sorting:
    def selection_sort(self,array):
        self.array = array
        n = len(self.array)

        for i in range(n-1):
            for j in range(i+1,n):
                if self.array[j]<self.array[i]:
                    self.array[j],self.array[i]=self.array[i],self.array[j]
        return self.array
    
    def bubble_sort(self,array):
        self.array = array
        n = len(self.array)

        for i in range(n):
            for j in range(0,n-i-1):
                if self.array[j]>self.array[j+1]:
                    self.array[j],self.array[j+1]=self.array[j+1],self.array[j]
        return array

    def insertion_sort(self,array):
        self.array = array
        n = len(self.array)

        for i in range(1,n):
            key = array[i]
            j = i-1

            while j>=0 and array[j]>key:
                array[j+1]=array[j]
                j-=1
            array[j+1]=key
        return self.array
    
    def shell_sort(self,arr):
        self.arr = arr
        gap = len(arr)//2

        while gap>0:

            for i in range(gap,len(arr)):
                j = i
                temp = arr[i]

                while j>=gap and arr[j-gap]>temp:
                    arr[j]= arr[j-gap]
                    j -=gap
                arr[j] =temp
            gap//=2

        return arr

sort = Sorting()
while True:
    print('-----------------------------------------')
    print(('|\t1.Selection sort\t\t|\n|\t2.Bubble sort\t\t\t|\n|\t3.Insertion sort\t\t|\n|\t4.Shell Sort\t\t\t|'))
    print('-----------------------------------------\n')
    choice = int(input('Select the sorting method:'))
    if choice == 1:
        size = int(input('enter the array size:'))
        print(f'enter {size} elements')
        array = [int(input()) for i in range(size)]
        result = sort.selection_sort(array)
        print(f'the sorted list is {result}')

    elif choice ==2:
        size = int(input('enter the array size:'))
        print(f'enter {size} elements')
        array = [int(input()) for i in range(size)]
        result = sort.bubble_sort(array)
        print(f'the sorted list is {result}')

    elif choice == 3:
        size = int(input('enter the array size:'))
        print(f'enter {size} elements')
        array = [int(input()) for i in range(size)]
        result = sort.insertion_sort(array)
        print(f'the sorted list is {result}')

    elif choice == 4:
        size = int(input('enter the array size:'))
        print(f'enter {size} elements')
        array = [int(input()) for i in range(size)]
        result = sort.shell_sort(array)
        print(f'the sorted list is {result}')

    else:
        break

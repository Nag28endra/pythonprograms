def BinarySearch(List,Value):
    low = 0
    high = len(List)-1
    while low <=high:
        mid = low + high//2
        num = List[mid]
        if num==Value:
            return int(mid)
        elif value>num:
            high = mid-1
        else:
            low = mid+1
    return None
myList = list(map(int,input('enter the values in the ascending order:').split()))
value = int(input('enter the value to be searched: '))
result=BinarySearch(myList,value)
print(f'{value} is found at the position {result}')
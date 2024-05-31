#juggling algorithm
def jugglingAlgo(arr,n,d):
    for i in range(d):
        temp = arr[0]
        for j in range(n-1):
            arr[j]=arr[j+1]
        arr[n-1]=temp
    print('the array after the rotation is {}'.format(arr))

values = list(map(int,input('enter the values').split()))

length = len(values)
rotations = int(input('enter the number of rotations:'))

print('the array before the rotation is {}'.format( values))
jugglingAlgo(values,length,rotations)
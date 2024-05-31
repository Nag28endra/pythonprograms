# Binary search using recursion
# def BinarySearch(array,left,right,val):
#     if right>=left:
#         mid = (right+left)//2
#         if array[mid]==val:
#             return mid+1
#         elif array[mid]<value:
#             return BinarySearch(array, mid+1, right, val)
#         else:
#             return BinarySearch(array,left,mid-1,val)
#     else:
#         return -1

# print('enter array elements:')
# array = [int(x) for x in input().split()]
# sorted_array = sorted(array)
# arr_length = len(sorted_array)
# print(f'the sorted array of given elements is {sorted_array}')
# value = int(input('enter the value to searched:'))
# pos = BinarySearch(sorted_array,0,arr_length-1,value)
# print(f'the element {value} is found at {pos} position')


#Merge Sort
def Merge_Sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = Merge_Sort(left)
    right = Merge_Sort(right)

    return MergeArray(left,right)

def MergeArray(left,right):
    result = []
    i=j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


print('enter the array elements:')
unsortedArray = [int(x) for x in input().split()]
sortedList = Merge_Sort(unsortedArray)
print(f'the sorted array is {sortedList}')
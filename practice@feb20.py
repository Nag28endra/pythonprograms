# # circular rotations of an array

# def circularRotations(arr,n,k):
#     i=0
#     while i<k:
#         k = k%n
#         arr = arr[n-k:]+arr[:n-k] # used for performing circular rotations
#         i += 1
#     return arr


# array = list(map(int,input('enter the array elements').split()))
# length = len(array)
# rotations = int(input('enter no of rotations:'))

# arr = circularRotations(array,length,rotations)
# print('array elements after rotation are: {}'.format(arr))

def wrap(string, max_width):
    new = ""
    i=0
    while string[i:(max_width+i)]!= "":
        new += string[i:(max_width+i)]+"\n"
        i += max_width
    return new
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result,end=' ')

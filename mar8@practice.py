# def ClosestElement(arr,l,target):
#     low =0
#     high = l-1
#     if arr[low]>=target:
#         return arr[0]
#     if arr[high] <= target:
#         return arr[high]
#     while low<high:
#         mid = (low+high)//2
#         if arr[mid]==target:
#             return arr[mid]
#         if arr[mid]>target:
#             if target> arr[mid-1]:
#                 if (target-arr[mid-1]>= arr[mid]-target):
#                     return arr[mid]
#                 else:
#                     return arr[mid-1]
#             high = mid
        
#         else:
#             if arr[mid]<target:
#                 if target<arr[mid+1]:
#                     if (target-arr[mid]>= arr[mid+1]-target):
#                         return arr[mid+1]
#                     else:
#                         return arr[mid]
#                 low = mid+1
#     return arr[mid]


# print('enter the array elements:')
# array = [int(x) for x in input().split()]
# sorted_array = sorted(array)
# length = len(sorted_array)
# print(f'the array is {sorted_array}')
# target = int(input('enter the target element:'))
# Closest_element = ClosestElement(sorted_array,length,target)
# print(f'the closest value to {target} is {Closest_element}')

# def count_necklaces(max_pearls, start_coeff, end_coeff):
#     # Base case
#     if max_pearls <= 0:
#         return end_coeff - start_coeff + 1
    
#     # Recursive case
#     count = 0
#     for coeff in range(start_coeff, end_coeff+1):
#         count += count_necklaces(max_pearls-1, coeff, end_coeff)
#     return count

# # Get user inputs
# max_pearls = int(input())
# start_coeff = int(input())
# end_coeff = int(input())

# # Call the function and print the output
# num_necklaces = count_necklaces(max_pearls, start_coeff, end_coeff)
# print(num_necklaces)

def count_necklaces(max_pearls, start_coeff, end_coeff):
    # Initialize count to 0
    count = 0
    
    # Loop through each possible combination of pearls
    for i in range(1, max_pearls+1):
        for j in range(start_coeff, end_coeff-i+2):
            # If we are at the last pearl, add 1 to the count
            if i == max_pearls:
                count += 1
            else:
                # Otherwise, continue with the next pearl
                for k in range(j, end_coeff+1):
                    count += count_necklaces(max_pearls-i, k, end_coeff)
    
    return count

# Example usage
max_pearls = int(input())
start_coeff = int(input())
end_coeff = int(input())

# Call the function and print the output
num_necklaces = count_necklaces(max_pearls, start_coeff, end_coeff)
print(num_necklaces)

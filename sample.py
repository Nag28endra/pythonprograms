# # # def shell_sort(arr):
# # #     n = len(arr)
# # #     gap = n // 2

# # #     while gap > 0:
# # #         for i in range(gap, n):
# # #             temp = arr[i]
# # #             j = i

# # #             while j >= gap and arr[j - gap] > temp:
# # #                 arr[j] = arr[j - gap]
# # #                 j -= gap

# # #             arr[j] = temp

# # #         gap //= 2

# # # # Example usage:
# # # arr = [64, 34, 25, 12, 22, 11, 90]
# # # shell_sort(arr)
# # # print("Sorted array:", arr)

# # # a = 7
# # # for i in range(5):
# # #     if (i==0):
# # #         print(a,end=" ")
# # #     elif (i%2!=0):
# # #         a -=2
# # #         print(a,end=" ")
# # #     else:
# # #         a +=3
# # #         print(a,end=" ")

# # # print(ascii(['']))

# # # def spam():
# # #     global eggs
# # #     eggs = 'jiraya'

# # # eggs = 'itachi'
# # # spam()
# # # # print(eggs)

# # # values = lambda x,y: x>y
# # # bool_value = values(12,28)
# # # if bool_value:
# # #     print('jiraya')
# # # else:
# # #     print('itachi')

# # # dict_a = {'a': 1, 'b': 2}
# # # dict_b = {'b': 3, 'c': 4}
# # # dict_c = {**dict_a, **dict_b}
# # # print(dict_c)

# # # print(
# # # """Dear Alice,
# # # Eve's cat has been arrested for catnapping,
# # # cat burglary, and extortion.
# # # Sincerely,
# # # Bob"""
# # # )

# # # # print('Hello Namratha'.center(20,"="))
# # # def generate_series(num):
# # #     series = ""
# # #     for i in range(1, num + 1):
# # #         line = ""
# # #         for j in range(1, i + 1):
# # #             line += str(j)
# # #             if j != i:
# # #                 line += "#"
# # #         series += line + "\n"
# # #     return series

# # # # Get user input
# # # n = int(input())

# # # # Generate and print the series
# # # result = generate_series(n)
# # # print(result)


# # # def find_permutations(string):
    
# # #     if len(string) == 0:
# # #         return []

 
# # #     if len(string) == 1:
# # #         return [string]

  
# # #     permutations = []

# # #     # Iterate through each character in the string
# # #     for i in range(len(string)):
# # #         # Extract the current character
# # #         current_char = string[i]

# # #         # Generate a new string without the current character
# # #         remaining_chars = string[:i] + string[i+1:]

# # #         # Recursively find permutations of the remaining characters
# # #         sub_permutations = find_permutations(remaining_chars)

# # #         # Add the current character to each permutation of the remaining characters
# # #         for permutation in sub_permutations:
# # #             permutations.append(current_char + permutation)

# # #     return permutations

# # # # Get user input
# # # input_string = input("Enter a string: ")

# # # # Find permutations of the string
# # # result = find_permutations(input_string)

# # # # Print the permutations
# # # print("Permutations:")
# # # for permutation in result:
# # #     print(permutation)


# # # def find_permutations(string):
   
# # #     if len(string) == 1:
# # #         return [string]
   
# # #     permutations = []

# # #     for i in range(len(string)):
      
# # #         current = string[i]
# # #         remaining = string[:i] + string[i + 1:]    
# # #         sub_permutations = find_permutations(remaining)        
# # #         for sub_permutation in sub_permutations:
# # #             permutations.append(current + sub_permutation)

# # #     return permutations
# # # input_string = input()
# # # result = find_permutations(input_string)
# # # print(result)

# # # def generate_series(a):
# # #     series = ""
# # #     for i in range(1, a + 1):
# # #         for j in range(i):
# # #             series += str(j + 1) + "#"
# # #         series = series[:-1]  # Remove the trailing "#" from the last number
# # #         series += "\n"  # Add a new line after each row
# # #     return series

# # # # Test the function
# # # input_num = int(input("Enter a number: "))
# # # output = generate_series(input_num)
# # # print(output)

# # def generate_output(n):
# #     output = ''
# #     for i in range(1, n + 1):
# #         row = ''
# #         for j in range(1, i + 1):
# #             row += str(j) + '#'
# #         output += row.rstrip('#') + '\n'
# #     return output

# # # Example usage
# # n = int(input("Enter a number: "))
# # output = generate_output(n)
# # print(output)

# def two_sum(numbers):
#     target = int(input())
#     numbers_length = len(numbers)
#     output=[]
#     for i in range(0,numbers_length+1):
#         for j in range(i+1,numbers_length):
#             if (numbers[i]+numbers[j]==target):
#                 output.extend([i,j])
#                 break
#     print(output)


# nums = [int(x) for x in input().split()]
# print(nums)
# two_sum(nums)

# x = 121
# temp = x
# rev=0
# while x!=0:
#     rem = x%10
#     rev = (rev*10)+rem
#     x = x/10
# if temp==rev:
#      print(True)
# else:
#     print(False)

# s = 'III'
# m = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
        
# ans = 0
        
# for i in range(len(s)):
#     if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
#         ans -= m[s[i]]
#     else:
#         ans += m[s[i]]
        
# # print(ans)
# v = ["flower","flow","flight"]
# ans=""
# v=sorted(v)
# print(v)
# first=v[0]
# last=v[-1]
# for i in range(min(len(first),len(last))):
#     if(first[i]!=last[i]):
#        print(ans)
#        break
#     ans+=first[i]
print(1001%910)
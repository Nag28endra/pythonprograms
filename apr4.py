# def outlier(arr):
#     even=[]
#     odd = []
#     for element in arr:
#         if element%2==0:
#             even.append(element)
#         else:
#             odd.append(element)
#     if len(even)==1:
#         return (even[0])
#     else:
#         return odd[0]



# print(outlier([160, 3, 1719, 19, 11, 13, -21]))

# def dig_pow(n, p):
#     temp = n 
#     length = len(str(n))
#     rev = 0
#     while n!=0:
#         dig = n %10
#         rev = (rev*10)+dig
#         n //=10
#     # print(rev)
#     sum = 0
#     for i in range(p,length+1):
#         value = rev%10
#         sum += pow(value,i)
#         rev //=10
#     # print(sum)
#     if sum!=temp:
#         return sum//temp
#     else:
#         return -1

# print(dig_pow(695, 2))


# def dig_pow(n, p):
#     # Convert n to a string and calculate the sum of the digits raised to successive powers of p
#     total = sum([int(digit)**(p+i) for i, digit in enumerate(str(n))])
    
#     # Calculate the value of k
#     k = total // n
    
#     # Check if k is an integer
#     if str(k).isnumeric():
#         return int(k)
#     else:
#         return -1

# print(dig_pow(695, 2))

# def persistence(n):
#     temp = n
#     mul = len(str(n))
#     count = 0
#     value = 1
#     if mul!=1:
#         while n!=0:
#             dig = n%10
#             value *= dig
#             n //=10
#         count +=1

#     print(count)
# # persistence(999)

# def generate_hashtag(s):
    
#     s=s.title()
#     print(s)
#     s= s.replace(' ','')
#     nstring = list(s)
#     nstring.insert(0, '#')
#     # print(nstring)

#     return ''.join(nstring)
# print(generate_hashtag('      Codewars'))
def move_zeros(lst):
    lst = lst.sort()
    zeros = []
    for item in lst:
        if item == 0:
            value = lst.remove(item)
            break
    print(value)
    print(zeros)


move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
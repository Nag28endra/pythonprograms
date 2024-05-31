# import pprint

# msg = 'hello samaritans,how are you people doing?'
# count = {}

# for character in msg:
#     count.setdefault(character,0)
#     count[character] += 1

# pprint.pprint(count)

# dict_keys = ['name','father name','power']
# dict_values = ['goku','bardock','autonomous ultra instinct']
# dictionary = dict(zip(dict_keys,dict_values))
# print(dictionary)

# dictionary = dict(name = "goku",father_name= "bardock",power ="autonomous ultra instinct" )
# print(dictionary)

# number = 371  #3^3 +7^3 + 1^3 = 371 is armstrong number
# length = len(str(number))
# sum = 0
# k = number

# while number != 0:
#     value = number %10
#     sum += pow(value,length)
#     number = number // 10

# if sum == k:
#     print('amrstrong')
# else:
#     print('not amrstrong')
# #Note:length should be considered based on the number of digits in the number

# ran= int(input())
# low, high = 2, ran
# primes = []

# for i in range(low, high + 1):
#     flag = 0

#     if i < 2:
#         continue
#     if i == 2:
#         primes.append(2)
#         continue

#     for x in range(2, i):
#         if i % x == 0:
#             flag = 1
#             break

#     if flag == 0:
#         primes.append(i)
        
# n1,n2= 0,1
# n3 = 0
# for i in range(2, ran+1):
#     val = str(primes).join(str(n3))
#     n3 = n1 + n2
#     print(val)    
#     n1 = n2
#     n2 = n3


num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()


    
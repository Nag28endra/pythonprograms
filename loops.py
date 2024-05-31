"""
                                    LOOPS:
    WE HAVE FOLLOWING LOOPS IN PYTHON;
            -FOR:
                syntax:
                            FOR <var_name> in range(param1,param2,param3):
                                    LOGIC

                                

            -WHILE
                    syntax:     WHILE CONDITION:
                                        LOGIC
                                        UPDATE STATEMENT
"""
# name = '' #this is empty string
# while name != 'vamsi':
#         name = input('enter your name:')
#         print(f'hello {name} welcome to python course')
# print('out of the loop')

# i = 0
# while i<5:
#         print('hello world')
#         i +=1
# print('out of the loop')

# name = ''
# while True:
#         name = input('enter your name:')
#         if name == 'vamsi' or name == 'Vamsi':
#                 break
# print(f'hello {name} welcome to python course')

# name = ''
# while True:
#         name = input('enter your name:')
#         if name !='vamsi':
#                 continue
#         print(f'hello {name} welcome to NASA basement')
#         password = input('enter the password:')
#         if password == '1234':
#                 print('permission granted!')
#                 break
# print('out of the loop')

# for i in range(0,10,3):
#         print(i)
# print('out of the loop')

n = int(input())
arr = map(int, input().split())[:-1]
print(arr)
print('this is an example for exception handling....')
try:
    with open('sample.txt','r') as obj:
        content = obj.read()
except :
    print('error occurred while opening the file')
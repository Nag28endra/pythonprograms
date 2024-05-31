# # use of lambda functions

# variable = lambda a : a +28
# print(variable(12))

# product = lambda a,b : a*b
# print(product(12,28))

def myLambda (value):
    return lambda a : a * value

myObject = myLambda(12)

print(myObject(28))
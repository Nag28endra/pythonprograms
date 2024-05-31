pattern = list(input("Enter the pattern:"))
string  = input("Enter the string:").split()
res = [()]

flag = 1
for p,s in zip(pattern,string):
    if ((p,s)in res):
        flag = 0
    res.append((p,s))

if flag == 1:
    print("true")
else:
    print("False")





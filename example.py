a = int(input())
b = int(input())
c = int(input())
small = a

if b<small and b<c:
    small = b
    print(small)
elif c<small and c<b:
    small =c 
    print(small)
else:
    print(small)
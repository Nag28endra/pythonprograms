a,b  = map(int,input().split())
Sum =0 
for i in range(a,b+1):
    st = str(i)
    l = list(st)
    m = int(max(l))
    s= 0
    for j in l:
        s+= int(j)
    if (s-m==m):
        Sum += int(i)
print(Sum)
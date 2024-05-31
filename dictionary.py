n = int(input())
volcanic = []
nonvolcanic =[]
result = []
for i in range(0,n):
    ele = int(input())
    volcanic.append(ele)
n2 = int(input())
for j in range (0,n2):
    val = int(input())
    nonvolcanic.append(val)
for i in volcanic:
    for j in nonvolcanic:
        if i == j:
            result.append(i)
            

for i in set(result):
    print(i)

def StockSpan(arr):
    for i in range(len(arr)):
        span = 1
        j = i-1
        while j>=0 and arr[j]<=arr[i]:
            span +=1
            j -=1
        print(span,end=" ")


arr = [int(x) for x in input().split()]
StockSpan(arr)
def isArrayInSortedOrder(A):
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isArrayInSortedOrder(A[1:])
A= [327, 220, 246, 277, 321, 454, 534, 565, 933]
print(isArrayInSortedOrder(A))
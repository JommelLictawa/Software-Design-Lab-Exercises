def findmin(A, n):
    if (n==1):
        return A[0]
    return min(A[n-1], findmin(A,n-1))

def findmax(A,n):
    if (n==1):
        return A[0]
    return max(A[n-1], findmax(A,n-1))

A = [-1,2,0,4,5,6,3,-9,-9.1]
n=len(A)
print("Data: ", A)
print("minimum: ",findmin(A,n))
print("maximum: ",findmax(A,n))

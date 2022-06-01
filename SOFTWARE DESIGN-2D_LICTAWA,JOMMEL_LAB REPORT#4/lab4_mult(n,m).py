def mult(m,n):
    if n == 1:
        return m
    else:
        return m + mult(m,n-1)

m = int(input("Enter m: "))
n = int(input("Enter n: "))
print ("Product: ",mult(m,n))

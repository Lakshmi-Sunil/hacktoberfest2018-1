def binary(n):
 if n==1:
  return 1
 else:
  return n%2 + (binary(n//2)*10)
n=int(input("Enter number:"))
c=binary(n)
print("Binary equivalent of ",n,"is ",c)


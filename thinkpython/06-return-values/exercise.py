# Write a boolean function, is_between(x, y, z), that returns True if  x<y<z  or if  z<y<x , and False otherwise.

def is_between(x, y, z):
  if x<y<z:
    return True
  elif z<y<x:
    return True
  else:
    return False
  
print(is_between(1, 2, 3))
print(is_between(3, 2, 1))
print(is_between(1, 3, 2))

# The Ackermann function,  A(m,n) , is defined:
# A(m,n) = n+1 if m = 0
# A(m,n) = A(m-1,1) if m > 0 and n = 0
# A(m,n) = A(m-1,A(m,n-1)) if m > 0 and n > 0
# Write a function named ackermann that evaluates the Ackermann function. What happens if you call ackermann(5, 5)?

def ackermann(m,n):
  if m == 0:
    return n + 1
  elif m > 0 and n == 0:
    return ackermann(m-1, 1)
  elif m > 0 and n > 0:
    return ackermann(m-1, ackermann(m, n-1))

print(ackermann(3, 2))
print(ackermann(6, 5)) # Throw RecursionError because the depth of recursion already exceeds Python's default limit

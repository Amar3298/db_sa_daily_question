def isPrime(n):
  if(n<2):
    return False
  for i in range(2,n):
    if(n%i==0):
      return False
  return True

def totalPrime(s,e):
    count = 0
    for i in range(s,e):
        if(isPrime(i)):
            count += 1
    return count
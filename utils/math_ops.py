# find even or not
def is_even_number(n):
  return n % 2 == 0

# find prime or not
def is_prime_number(n):
  if n <=1 :
    return False
  for i in range(2, n):
    if n % 2 == 0:
      return False
  return True

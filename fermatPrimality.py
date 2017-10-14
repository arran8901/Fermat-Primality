# Probable prime test using Fermat's Little Theorem

# Number of checks - number of bases to check before deducing primality
# Bases start at 2 and increase but never divides into p
# Increase number of checks to avoid Fermat liars / pseudoprimes
numberOfChecks = 2

p = input("Insert number to check prime: ")

if p == 2 or p == 3:
  print True
else:
  for b in range(2, p - 1):
    if b % p != 0:
      print (b ** (p - 1)) % p == 1
      numberOfChecks -= 1
    if numberOfChecks == 0:
      break
# Fermat-Primality
Probable prime test using Fermat's Little Theorem

Fermat's Little Theorem states that:
a^(p-1) ≡ 1 (mod p)
where a is any integer, p is a prime number, and p is not divisible by a

Thus p can be tested for primality without any knowledge of p's factors

Note that there are instances where a composite number may yield 1. Such values are called Fermat liars.
The algorithm enables the testing of the equality with more values of 'a' by increasing the variable numberOfChecks.

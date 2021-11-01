# Cryptomath Module
# https://www.nostarch.com/crackingcodes (BSD Licensed)

def gcd(a, b):
    # Return the Greatest Common Divisor of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Return the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # No mod inverse exists if a & m aren't relatively prime.

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # Note that // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def lcm(a, b):
    # Return the Least Common Multiple of a and b
    if a and b and a != 0 and b !=0:
        return abs(a // gcd(a, b) * b)
    else:
        return 0
    
def findBezout(a, m):
    #this is the findModInverse function, modified to return the
    #  Bezout coefficients
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1,u2

#initial RSA but with phi n
p=131
q=157
n=p*q
phin=(p-1)*(q-1)
e=1337
eq1=gcd(e,phin)
d=findModInverse(e,n)
print(eq1)
print(n)

#encrypt
message=int(input('number for message'))

print(message)
encrypt=pow(message,e,n)
print(encrypt)

#decrypt
decrypt=pow(encrypt,d,n)

print(decrypt)


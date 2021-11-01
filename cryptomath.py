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


c1=3348898614019888901908403254933640035246212844961838831090198209986980794381721549119817432681384755697410365192319104804164099565189541033745677177908430898159000425144231080271489963068735078029094600990872466478190741629812176
e1=927497329847987298271115
m1=4035789025935566763434217693291904203514985559759202218772232737779637242777118595044390460183072421339720558176591333566629680159420540355202801063004396853930869779589477542063791290354739283500845851153515283182096350655220153

c2=239640052909589767377717332389707447467040807634556900631678847178249840124011908871933438491107613018104449557989400002181849114477870950132116542696807901617211160049032412890334084433427701567750018959947232564370889351855337
e2=123132131231124141411111
m2=4035789025935566763434217693291904203514985559759202218772232737779637242777118595044390460183072421339720558176591333566629680159420540355202801063004396853930869779589477542063791290354739283500845851153515283182096350655220153

u1,u2=findBezout(e1,e2)
print(u1,u2)
c2i=findModInverse(c2,m2)
print(c2i)
p1=pow(c1,u1,m2)
print(p1)
p2=pow(c2i,-u2,m2)
print(p2)
p3=p1*p2
ans=p3%m2
print(ans)

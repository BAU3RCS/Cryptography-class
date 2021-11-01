#Uses the primeNum module from

#https://nostarch.com/download/CrackingCodesFiles.zip

#Unzip the files and put primeNum.py into the directory you

#  call Python from.

import primeNum

 

# get a list of prime numbers

# using 7000 will get about 900 primes

primes = primeNum.primeSieve(7000)

 

#check to see if (p-1)/2 is a prime so p is "safe"

safe = []

 

for p in primes:

    if primeNum.isPrime( int((p-1)/2) ):

        safe.append(p)

 

print(safe)

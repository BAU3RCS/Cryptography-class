# Python3 code to find largest prime 
# factor of number 
import math 
  
# A function to find largest prime factor 
def maxPrimeFactors (n): 
      
    # Initialize the maximum prime factor 
    # variable with the lowest one 
    maxPrime = -1
      
    # Print the number of 2s that divide n 
    while n % 2 == 0: 
        maxPrime = 2
        n >>= 1     # equivalent to n /= 2 
          
    # n must be odd at this point,  
    # thus skip the even numbers and  
    # iterate only for odd integers 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
      
    # This condition is to handle the  
    # case when n is a prime number  
    # greater than 2 
    if n > 2: 
        maxPrime = n 
      
    return int(maxPrime) 
  
# Driver code to test above function 
#n = 15
#print(maxPrimeFactors(n)) 
  
n =4035789025935566763434217693291904203514985559759202218772232737779637242777118595044390460183072421339720558176591333566629680159420540355202801063004396853930869779589477542063791290354739283500845851153515283182096350655220153

 #input("n or m")
print(maxPrimeFactors(n)) 
  

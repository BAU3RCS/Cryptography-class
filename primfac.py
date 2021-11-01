def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors


pfs = prime_factors(10000000)
largest_prime_factor = max(pfs) # The largest element in the prime factor list
prime_factors(4035789025935566763434217693291904203514985559759202218772232737779637242777118595044390460183072421339720558176591333566629680159420540355202801063004396853930869779589477542063791290354739283500845851153515283182096350655220153)

def isprime(n: int):
    # brute force approach
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    
    if count > 2: return False
    return True

def count_primes(n: int):
    # use the optimal algorithm - Sieve of Erastosthenes
    isP = [True] * (n+1)
    count = 0

    for i in range(2, n+1):
        if isP[i]:
            count += 1

            for j in range(i*i, n, i):
                isP[j] = False
    
    return count

print(count_primes(11))
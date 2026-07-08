def gcd(a: int, b: int):
    gcd = 1
    n = min(a, b)
    m = max(a,b)
    
    if m%n == 0: return n

    for i in range(1,n+1):
        if a%i == 0 and b%i == 0:
            gcd = i
    
    return gcd

def optimal_gcd(a: int, b: int):
    # use the formula - gcd(a,b) = gcd(a-b, b) if a>b, or gcd(a,b-a) if b>a
    if a == 0: return b
    if b == 0: return a

    if a > b: return gcd(a-b, b)
    return gcd(a, b-a)

def least_common_multiple(a: int, b: int):
    # brute force
    candidate = max(a, b)

    while True:
        if candidate % a == 0 and candidate % b == 0:
            return candidate
        candidate += 1  

def lcm(a: int, b: int):
    gcd = optimal_gcd(a,b)

    return int((a*b/gcd))

print(lcm(3,25))
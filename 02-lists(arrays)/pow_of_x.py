# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000

def myPow(x: float, n: int) -> float:
    # use binary number logic here
    ans = 1
    if n < 0:
        x = 1/x
        n = -n
    while n > 0:
        if n % 2 == 1:
            ans = ans * x
        x = x*x
        n = n // 2
    
    return ans

print(myPow(2.0,10))
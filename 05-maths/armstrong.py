# An Armstrong number is a number that equals the sum of its own digits, each raised to the power of the total number of digits. For example, \(153\) is an Armstrong number because it has \(3\) digits, and \(1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153\).

def isArmstrong(n: int):
    sum = 0
    nums = [int(digit) for digit in str(n)]

    for digit in nums:
        sum += pow(digit, 3)
    
    return n == sum

print(isArmstrong(153))

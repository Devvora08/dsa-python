# // Given an array of characters chars, compress it using the following algorithm:
# // Begin with an empty string s. For each group of consecutive repeating characters in chars:

# // If the group's length is 1, append the character to s.
# // Otherwise, append the character followed by the group's length.
# // The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# // After you are done modifying the input array, return the new length of the array.
# // You must write an algorithm that uses only constant extra space.
# // Note: The characters in the array beyond the returned length do not matter and should be ignored.

# // Example 1:

# // Input: chars = ["a","a","b","b","c","c","c"] - [a,2,b,2,c,3] - 6
# // Output: 6

def compress(s):
    i = 0
    idx = 0

    while i < len(s):
        c = s[i]
        count = 0

        while i < len(s) and s[i] == c:
            count += 1
            i += 1

        s[idx] = c
        idx += 1

        if count > 1:
            for digit in str(count):
                s[idx] = digit
                idx += 1

    return idx

s = ['a','a','a','b','b','c','c','d','d','d']
print(compress(s))

            




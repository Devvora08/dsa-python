# // Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

# // Find the leftmost occurrence of the substring part and remove it from s.
# // Return s after removing all occurrences of part.
# // A substring is a contiguous sequence of characters in a string.

# // Example 1:

# // Input: s = "daabcbaabcbc", part = "abc"
# // Output: "dab"

def remove_occurence(s: str, part: str):
    while s.find(part) != -1:
        s = s.replace(part, "")
    
    return s

print(remove_occurence("daabcbaabcbc", "abc"))
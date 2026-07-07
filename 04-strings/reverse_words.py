# reverse words in string
# Example - Hi Dev ---> Dev Hi

def reverse_string(s: str):
    entirelyReversed = reversed(s)
    entirelyReversed = "".join(entirelyReversed)

    words = entirelyReversed.split(" ")

    ans = ""

    for word in words:
        rev = reversed(word)
        rev = "".join(rev)

        ans += rev + " "
    return ans

print(reverse_string("hi dev"))
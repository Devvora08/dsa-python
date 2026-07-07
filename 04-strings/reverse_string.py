# reverse string in place

def reverse(s):
    s = list(s)

    st = 0
    e = len(s)-1

    while st < e:
        temp = s[st]
        s[st] = s[e]
        s[e] = temp

        st += 1
        e -= 1

    return "".join(s)

print(reverse("abcd"))
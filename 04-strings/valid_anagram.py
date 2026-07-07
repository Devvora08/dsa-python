# check if input s1, s2 are anagrams

def isAnagram(s1: str, s2: str):
    if len(s1) != len(s2): return False

    # multiple approaches - sort and compare, dict, freq array
    s1 = list(s1)
    s2 = list(s2)

    s1dict = {}
    for c in s1:
        s1dict[c] = s1dict.get(c,0) + 1
    
    for c in s2:
        s1dict[c] = s1dict.get(c,0) - 1

    for v in s1dict.values():
        if v > 0: return False
    return True

print(isAnagram("abcd", "dxab"))
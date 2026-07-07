# // Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# // In other words, return true if one of s1's permutations is the substring of s2.

# // Example 1:

# // Input: s1 = "ab", s2 = "eidbaooo"
# // Output: true
# // Explanation: s2 contains one permutation of s1 ("ba").

def isFreqSame(l1: list, l2: list):
    for i in range(len(l1)):
        if l1[i] != l2[i]: return False
    
    return True

def isPermutation(s1: str, s2: str):
    freq = [0] * 26

    # initialize s1 frequency
    for i in range(len(s1)):
        idx = ord(s1[i]) - ord('a')
        freq[idx] += 1
    
    windowSize = len(s1)

    for i in range(len(s2)):
        windowIdx = 0
        idx = i

        windowFreq = [0] * 26

        while windowIdx < windowSize and idx < len(s2):
            windowFreq[ord(s2[idx]) - ord('a')] += 1
            windowIdx += 1
            idx += 1
        
        if isFreqSame(freq, windowFreq):
            return True
    
    return False

def useDict(s1: str, s2: str):
    # create a dict of frequencies
    freqs1 = {}
    for i in range(len(s1)):
        freqs1[s1[i]] = freqs1.get(s1[i], 0) + 1
    
    window = len(s1)
    
    for i in range(len(s2) - window + 1):
        winFreq = {}

        for j in range(i, i+window):
            winFreq[s2[j]] = winFreq.get(s2[j], 0) + 1

        if winFreq == freqs1 : return True
    return False


print(useDict("ab", "eidbaoo"))
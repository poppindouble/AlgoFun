from copy import deepcopy

def minWindow(s, t):
    dict1 = {}
    dict2 = {}
    for c in t:
        if c not in dict1:
            dict1[c] = 1
            dict2[c] = 1
        else:
            dict1[c] += 1
            dict2[c] += 1
    start = 0
    minStart = 0
    minSize = len(s) + 1
    count = len(t)
    for end, char in enumerate(s):
        if char in dict2 and dict2[char] > 0:
            dict1[char] -= 1
            if dict1[char] >= 0:
                count -= 1
        if count == 0:
            while True:
                if s[start] in dict2 and dict2[s[start]] > 0:
                    dict1[s[start]] += 1
                    if dict1[s[start]] < 0:
                        dict1[s[start]] += 1
                    else:
                        break
                start += 1
            if minSize > end - start + 1:
                minSize = end - start + 1
                minStart = start
    if minSize == len(s) + 1:
        return ""
    return s[minStart:minStart+minSize]


print(minWindow("ADOBECODEBANC", "ABC"))
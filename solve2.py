def solve(s):
    upper = 0
    low = 0
    for i in range(len(s)):
        if 64 < ord(s[i]) < 91:
            upper += 1
        else:
            low += 1
    if low > upper or low == upper:
        return s.lower()
    else:
        return s.upper()
print(solve("CODe"))
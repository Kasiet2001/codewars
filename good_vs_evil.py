def good_vs_evil(good, evil):
    g = good.split()
    e = evil.split()
    good = int(g[0]) + int(g[1]) * 2 + (int(g[2]) + int(g[3]) * 3) + int(g[4]) * 4 + int(g[5]) * 10
    evil = int(e[0]) + (int(e[1]) + int(e[2]) + int(e[3])) * 2 + int(e[4]) * 3 + int(e[5]) * 5 + int(e[6]) * 10
    if good > evil:
        return 'Battle Result: Good triumphs over Evil'
    elif evil > good:
        return 'Battle Result: Evil eradicates all trace of Good'
    return 'Battle Result: No victor on this battle field'
print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
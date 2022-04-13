def capitals(word):
    return [i for i in range(len(word)) if word[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
print(capitals('CodEWaRs'))
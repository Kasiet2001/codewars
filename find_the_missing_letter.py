def find_missing_letter(chars):
    ords = [ord(i) for i in chars]
    o = set([i for i in range(ords[0], ords[-1] + 1)]) - set(ords)
    return chr([i for i in o][0])
print(find_missing_letter(['O','Q','R','S']))
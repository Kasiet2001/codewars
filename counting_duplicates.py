def duplicate_count(text):
    dupl = 0
    from collections import Counter
    a = dict(Counter(text.lower()))
    for value in a.values():
        if value > 1:
            dupl += 1
    return dupl
print(duplicate_count("Indivisibilities"))
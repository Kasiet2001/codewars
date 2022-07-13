def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    unique = [iterable[0]]
    for i in iterable:
        if i != unique[-1]:
            unique.append(i)
    return unique
print(unique_in_order(''))

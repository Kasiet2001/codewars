def abbrev_name(name):
    return f'{name.title().split()[0][0]}.{name.title().split()[1][0]}'
print(abbrev_name("Sam H"))
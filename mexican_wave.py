def wave(people):
    return [people[:i] + people[i].upper() + people[i + 1:] for i in range(len(people)) if people[i] != ' ']
print(wave('two words'))


def wave(people):
    wave = []
    for i in range(len(people)):
        if people[i] != ' ':
            wave.append(people[:i] + people[i].upper() + people[i + 1:])
    return wave
print(wave('two words'))
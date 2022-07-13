def pig_it(text):
    list = text.split()
    return ' '.join([i[1:] + i[0] + 'ay' if i.isalpha() else i for i in list])
print(pig_it('Pig latin is cool ?'))
def to_camel_case(text):
    t = []
    if len(text) != 0:
        text = text.replace('_', ' ')
        text = text.replace('-', ' ').split()
        t.append(text[0])
        for i in range(1, len(text)):
            t.append(text[i].capitalize())
        return ''.join(t)
    return text
print(to_camel_case(""))
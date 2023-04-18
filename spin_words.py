def spin_words(sentence):
    words = sentence.split()
    s_w = []
    for i in words:
        if len(i) >= 5:
            s_w.append(i[::-1])
        else:
            s_w.append(i)
    return ' '.join(s_w)
print(spin_words("Hey fellow warriors"))


def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
def order(sentence):
    sentence = sentence.split()
    ordered_sentence = []
    for i in range(len(sentence) + 1):
        for j in sentence:
            if str(i) in j:
                ordered_sentence.append(j)
    ordered_sentence = ' '.join(ordered_sentence)
    return ordered_sentence
print(order("is2 Thi1s T4est 3a"))
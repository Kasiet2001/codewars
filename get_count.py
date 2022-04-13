def get_count(sentence):
    total = 0
    for i in range(len(sentence)):
        if sentence[i] == 'a' or sentence[i] == 'e' or sentence[i] == 'i' or sentence[i] == 'o' or sentence[i] == 'u':
            total += 1
    return total
print(get_count("abracadabra"))
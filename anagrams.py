def anagrams(word, words):
    return [anag for anag in words if sorted(word) == sorted(anag)]
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
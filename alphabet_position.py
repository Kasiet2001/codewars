def alphabet_position(text):
    a_p = [str(ord(i) - 96) for i in text.lower() if i.isalpha()]
    return ' '.join(a_p)
print(alphabet_position("The sunset sets at twelve o' clock."))
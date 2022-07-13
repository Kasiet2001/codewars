import string
def is_pangram(s):
    return len(set(string.ascii_lowercase)) <= len(set(s.lower()))
print(is_pangram("The quick brown fox jumps over the lazy!"))
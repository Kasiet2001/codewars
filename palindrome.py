def palindrome(x):
    return True if str(x) == str(x)[::-1] else False
print(palindrome(122))

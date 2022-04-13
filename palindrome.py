def palindrome(num):
    if type(num) is int and num >= 0:
        if str(num) == str(num)[::-1]:
            return True
        else:
            return False
    else:
        return 'Not valid'
print(palindrome(121))

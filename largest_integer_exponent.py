def get_exponent(n, p):
    exp = 0
    if p <= 1 or n == 1 or n == 0:
        return None
    elif p >= 2:
        while n % p == 0:
            exp += 1
            n /= p
        return exp
print(get_exponent(0,0))

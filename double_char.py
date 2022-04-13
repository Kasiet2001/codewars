def double_char(s):
    double = str()
    for i in s:
        double += i * 2
    return double
print(double_char("Hello World"))
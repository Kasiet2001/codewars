def expanded_form(num):
    form = []
    div = '10'
    while num != 0:
        if num % int(div) > 0:
            form.append(str(num % int(div)))
        num = num - num % int(div)
        div += '0'
    return ' + '.join(form[::-1])
print(expanded_form(70304))
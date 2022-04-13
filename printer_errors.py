def printer_error(s):
    errors = 0
    for i in s:
        if ord(i) > ord('m'):
            errors += 1
    return f'{errors}/{len(s)}'
print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
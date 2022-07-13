def sort_my_string(s):
    odd = list(s[i] for i in range(0, len(s), 2))
    even = [s[i] for i in range(1, len(s), 2)]
    return f"{''.join(odd)} {''.join(even)}"
print(sort_my_string("YCOLUE'VREER"))



def sort_my_string(s):
    return f'{s[::2]} {s[1::2]}'
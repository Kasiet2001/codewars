def ghostbusters(building):
    ghost = str()
    if " " in building:
        for i in building:
            if 97 <= ord(i.lower()) <= 122:
                ghost += i
        return ghost
    return "You just wanted my autograph didn't you?"
print(ghostbusters("BusStation"))
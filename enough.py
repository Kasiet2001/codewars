def enough(cap, on, wait):
    return on + wait - cap if cap < on + wait else 0
print(enough(20, 5, 5))
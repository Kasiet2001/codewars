def pillars(num_pill, dist, width):
    return (num_pill - 1) * (100 * dist) + ((num_pill - 2) * width) if num_pill > 1 else 0
print(pillars(11, 15, 30))
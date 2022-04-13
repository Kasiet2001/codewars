def inverse_slice(items, a, b):
    return items[:a] + items[b:]
print(inverse_slice(['Intuition', 'is', 'a', 'poor', 'guide', 'when', 'facing', 'probabilistic', 'evidence'], 5, 13))
def number_of_pairs(gloves):
    return sum(gloves.count(i)//2 for i in set(gloves))
print(number_of_pairs(['Blue', 'Gray', 'Yellow', 'Fuchsia', 'Teal', 'Olive', 'Yellow', 'Lime', 'Lime', 'Navy', 'Black', 'Yellow', 'Black', 'Silver', 'White']))
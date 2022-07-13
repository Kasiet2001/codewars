def cakes(recipe, available):
    a = []
    if len(available) < len(recipe):
        return 0
    for i in available:
        if i not in recipe:
            available[i] = 0
    for j in recipe:
        if j in available:
            a.append(available[j] // recipe[j])
    return min(a) if len(a) == len(recipe) else 0

def cakes(recipe, available):
    return min([available[i] // recipe[i] if i in available else 0 for i in recipe])
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))
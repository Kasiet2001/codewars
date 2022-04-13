def well(x):
    if x.count('good') == 0:
        return 'Fail!'
    elif x.count('good') > 2:
        return 'I smell a series!'
    else:
        return 'Publish!'
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))
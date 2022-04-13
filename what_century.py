def what_century(year):
    century = 0
    if int(year) % 100 != 0:
        century = (int(year) // 100 + 1)
    elif int(year) % 100 == 0:
        century = int(year) // 100
    if str(century)[-1] == '1' and str(century)[0] != '1':
        return str(century) + 'st'
    elif str(century)[-1] == '2' and str(century)[0] != '1':
        return str(century) + 'nd'
    elif str(century)[-1] == '3'and str(century)[0] != '1':
        return str(century) + 'rd'
    else:
        return str(century) + 'th'
print(what_century("2011"))
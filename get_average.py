def get_average(lst):
    return round(sum(i['age'] for i in lst) / len(lst))
print(get_average(lst = [
    {'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel', 'continent': 'Asia', 'age': 20, 'language': 'Ruby'},
    {'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania', 'continent': 'Europe', 'age': 21, 'language': 'C'},

    ]))
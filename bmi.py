def bmi(weight, height):
    body_mass = weight/height**2
    if body_mass <= 18.5:
        return 'Underweight'
    elif body_mass <= 25.0:
        return 'Normal'
    elif body_mass <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'
print(bmi(80, 1.80))


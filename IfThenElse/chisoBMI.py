__author__ = 'thangvv'
print('')

print('Enter your weight in pounds: ')
weight = int(input())
print('Enter your height in inches: ')
height = int(input())
weight = weight * 0.45359237
height = height * 0.0254

bmi = height / (weight * weight)

if bmi < 18.5:
    print('Underweight')
elif 18.5 <= bmi <25.0:
    print('Normal')
elif 25.0 < bmi < 30.0:
    print('Overweight')
else:
    print('Obese')

def calc_BMI():

    print('Body Mass Index(BMI) Calculator')
    print('-------------------------------')

    weight = float(input('Enter Your Weight(in kg): '))
    height = float(input('Enter Your Height(in meters): '))
    bmi = round(weight/(height)**2,2)
    print('Your BMI is',bmi)

    if bmi < 18.5 : 
        print('You are under weight!')
    elif 18.5 < bmi < 24.9:
        print('You have the Normal weight')   
    elif 25 < bmi < 29.9:
        print('You are over weight!')
    else:
        print('Dangerous, you have obesity!!')

calc_BMI()  





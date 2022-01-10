#Body mass index
question= input ("Do you want to check BMI?")
print(question)
if question=='yes':
    weight= input('What is your weight in kilograms?')
    print(weight)
    weight=int(weight)
    height= input('What is your height in meters?')
    print(height)
    height=float(height)
    BMI= weight/(height**2)
    Name= input('Your name?')
    print("Name")
    print(Name,',your BMI is', BMI )
else:
    print('Sorry, this site is not for you.')

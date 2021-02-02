# Python Program to find the bmi of a person


weight = float(input('Enter weight in kg: '))
height = float(input('Enter height in cm: '))

# calculate the bmi
bmi = weight / ((height /100)**2)


print('The bmi of the person is %0.4f' %bmi)


#CREATE A BMI CALCULATOR
height = input("Enter your height in M:")
weight = input("Enter your weight in Kg:")
print(type(height))
print(type(weight))
#BMI=WEIGHT(kg)/HEIGHT^2(m^2)
Body_mass_index = int(weight) / float(height)**2
z = int(Body_mass_index)
print("Your BMI is:" + str(z))
#create a program using maths and f-strings that tell us how many days, weeks, and months we have left if we live 
#upto 90 years old
#it will take your current age as input and output a message with your time left in this format
#You have x days, y weeks and z months left

#current age
age = input("What is your current age: ")
total_years = 90
remaining_years = 90 - int (age)
days = remaining_years * 365
weeks = remaining_years * 52
months = remaining_years * 12
print(f" You have {days} days, {weeks} weeks, and {months} months")
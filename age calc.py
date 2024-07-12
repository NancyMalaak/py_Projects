age = input("What is your current age?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remainig = years_remaining * 365
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
print (f"You have {days_remainig} days, {months_remaining} months, {weeks_remaining} weeks left.")

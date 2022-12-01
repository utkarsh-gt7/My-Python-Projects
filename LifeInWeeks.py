age = input("What is your current age?")

age_int=int(age)
days_left=(90-age_int)*365
weeks_left=(90-age_int)*52
months_left=(90-age_int)*12
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

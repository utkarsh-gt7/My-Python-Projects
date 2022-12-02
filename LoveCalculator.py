print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name=name1+name2
lcombined_name=combined_name.lower()

t=lcombined_name.count('t')
r=lcombined_name.count('r')
u=lcombined_name.count('u')
e=lcombined_name.count('e')

l=lcombined_name.count('l')
o=lcombined_name.count('o')
v=lcombined_name.count('v')
e=lcombined_name.count('e')

digit1=t+r+u+e
digit2=l+o+v+e

score=int(str(digit1)+str(digit2))

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


i=0
letters_char=""
while i<nr_letters:
  letter_index=random.randint(0,len(letters)-1)
  i+=1
  a=letters[letter_index]
  letters_char+=a
print(letters_char)

j=0
symbols_char=""
while j<nr_symbols:
  symbol_index=random.randint(0,len(symbols)-1)
  j+=1
  b=symbols[symbol_index]
  symbols_char+=b
print(symbols_char)

k=0
numbers_char=""
while k<nr_numbers:
  number_index=random.randint(0,len(numbers)-1)
  k+=1
  c=numbers[number_index]
  numbers_char+=c
print(numbers_char)

password=letters_char+symbols_char+numbers_char

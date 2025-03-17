'''
Name Cases:
Use a variable to represent a person’s name, and then print that person’s name in
lowercase, uppercase, and title case.
'''

nome: str = "Dioni"

lowercase = nome.lower()
uppercase = nome.upper()
title = nome.title()

print(f"{lowercase}, {uppercase}, {title}")

# # #  metodo alternativo
# # print(nome.lower()) 
# # print(nome.upper())
# # print(nome.title())
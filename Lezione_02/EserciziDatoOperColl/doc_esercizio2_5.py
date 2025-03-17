'''
2-5: Famous Quote:
Find a quote from a famous person you admire.
Print the quote and the name of its author.
Your output should look something like the following,
including the quotation marks: Albert Einstein once said,
“A person who never made a mistake never tried anything new.”
:::
2-6: Famous Quote 2:
Repeat Exercise 2-5, but this time,
represent the famous person’s name using a variable called famous_person.
Then compose your message and represent it with a new variable called message.
Print your message.
'''

autore: str = "Kit Carson"
cit: str = "Mai fasciarsi la testa prima di essersela rotta"

print(f'{autore} una volta disse: "{cit}"')

# le apici vanno in conflitto tra di loro se uguali, usare \" ... \" per forzare le virgolette
# print(f"{autore} una volta disse: \"{cit}\"")
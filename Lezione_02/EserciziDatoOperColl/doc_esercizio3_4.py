'''
Guest List:
If you could invite anyone, living or deceased, to dinner,
who would you invite?
Make a list that includes at least three people you’d like to invite to dinner.
Then use your list to print a message to each person,
inviting them to dinner
'''

dinner: list = ["Chopin", "Mozart", "Bach"]

for i in dinner:

    print(f" Sig. {i}, è invitato a cena!")
    
dinner: list = ["Chopin", "Mozart", "Bach"]

print("Sei invitato alla cena " + dinner[0])
print("Sei invitato alla cena " + dinner[1])
print("Sei invitato alla cena " + dinner[2])
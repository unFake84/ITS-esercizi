n: int = int(input("How old are you?: "))

if n < 2:

    print("You are a baby!")

elif n >= 2 and n < 4:

    print("You're a toddler!")

elif n >= 4 and n < 13:

    print("You're a kid!")

elif n >= 13 and n < 20:

    print("You're a teenager!")

elif n >= 20 and n < 65:

    print("You're an adult!")

elif n >= 65 and n < 110:

    print("You're an elder!")

else:

    print("You are Godlike!")
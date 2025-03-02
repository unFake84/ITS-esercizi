#current_users: list[str] = ["Alpha", "Beta", "Charlie", "Delta", "Echo"]
current_users: list[str] = ["alpha", "beta", "charlie", "delta", "echo"]
new_users: list[str] = ["Foxtrot", "Alpha", "Golf", "Echo", "India", "BETA", "deLTa"]

print(".----------------------------------------------------------------------.")
print(f"|          [[{current_users}]]           |")
print(f"|  [[{new_users}]]  |")
print("'----------------------------------------------------------------------'")

for user in new_users:

    if user.lower() in current_users:

        print(f"[{user}] username already been used, please change it.")

    else:

        print(f"[{user}] is avaiable. Please proceed.")
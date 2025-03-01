#current_users: list[str] = ["Alpha", "Beta", "Charlie", "Delta", "Echo"]
current_users: list[str] = ["alpha", "beta", "charlie", "delta", "echo"]
new_users: list[str] = ["Foxtrot", "Alpha", "Golf", "Echo", "India", "BETA"]

for user in new_users:

    if user.lower() in current_users or user.title() in current_users:

        print(f"[{user}] username already been used, please change it.")

    else:

        print(f"[{user}] is avaiable. Please proceed.")
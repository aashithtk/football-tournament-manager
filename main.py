from tournament import Tournament

t = Tournament()

while True:
    print("\nFootball Tournament Manager")
    print("1 Add Team")
    print("2 Show Table")
    print("3 Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Team name: ")
        t.add_team(name)

    elif choice == "2":
        table = t.get_table()
        for team in table:
            print(team)

    elif choice == "3":
        break

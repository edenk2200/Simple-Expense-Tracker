import datetime

today = datetime.date.today().strftime("%d/%m/%y")
allowed_categories = ["tech", "academics", "tools", "essentials", "food", "transport"]

while True:
    print(f"1. Add a new expense")
    print(f"2. Read your current expenses")
    print(f"3. Exit")

    choice = str(input("Select an option (1, 2 or 3): "))

    if choice == "1":
        amt_spent = (input("Input the amount spent: "))
        while True:
            try:
                amt_spent = float(amt_spent)
                break
            except ValueError:
                print(f'{amt_spent} is not valid. Please enter a valid value for the amount spent.')
                amt_spent = input("Please input a new value ")
        item_spent = str(input("What did you spend on? ").lower())
        category_spent = str(input("What category? ").lower())
        
        while category_spent not in allowed_categories:
            print(f"{category_spent} is an invalid category. Please try again.")
            category_spent = str(input("What category? ").lower())
        try:
            with open("expenses.txt", "a") as file:
                file.write(f"{today} | {amt_spent} | {item_spent} | {category_spent}\n")
            print(f"Successful Operation. Added {amt_spent} | {item_spent} | {category_spent}\n")
        except IOError as e:
            print(f"An I/O Error Occurred: {e}")
            
    elif choice == "2":
        try:
            with open("expenses.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print(f"Error: The file was not found")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == "3":
        print("Bye and thanks for using my expense tracker!")
        break

    else:
        print(f"Invalid Input. Please Try Again.")

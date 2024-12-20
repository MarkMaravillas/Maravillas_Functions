# Mark Daniel's Menu
Menu = {"Pizza": 120, "Burger": 150, "Fries": 80, "Soda": 50, "Sundae": 45, "Fillet": 100, "Chicken": 160, "Rice": 30}  # I Used Dictionary To Set Food And Their Respective Price Values

Purchase = []
Total = 0

def display_menu(Menu):
    print("======= Welcome to Mark Daniel's Can I Get Your Order? =====")  # MAIN MENU OUTPUT FOR THE USER REFERENCE W/ ADDTION OF SPACING AND DECIMAL POINT
    for Food, value in Menu.items():
        print(f"{Food:10} : {value:.2f}")
    print("=============================================================")


def take_order(Menu, Purchase):
    while True:  # To Indefinitely ask the user for order until they type in "Done"
        print(f"Here Is The List Of Your Orders: {Purchase}")  # Addition of live stored menu items every iteration of the loop.
        print()
        Order = input(f"""May I take Your Order? ("done" to quit): """).title()

        if Order.lower() == "done":  # Allows for any iteration of "DONE" to be typed
            break
        elif Order == "":
            print()
            print("Please Select an Order")
        elif Menu.get(Order) is not None:  # It will only store user-input that are not the "None" value in the Dictionary.
            Purchase.append(Order)


def calculate_total(Purchase, Menu):
    Total = 0
    for items in Purchase:  # Calculate the total value of each ordered items
        Total += Menu.get(items)
    return Total


def confirm_order(Purchase, Menu, Total):
    while True:
        print()
        print(f"Is The Order Correct? Please Confirm Your Purchase: {Purchase}")  # Let's the user check if their order is correct
        print()
        Confirm = input("Y = yes , N = no or A = To Add More Items: ")  # Added option to confirm, cancel and add more items to the Order

        if Confirm.upper() == "N":  # Cancellation of Items
            print()
            print("Please Try Again.")
            print()
            return False

        elif Confirm.upper() == "A":  # Addtion of Items
            while True:
                print(f"Here Is The List Of Your Orders: {Purchase}")  # Live display of items each Iteration
                print()
                Add = input(f"""Please Add Your additional Items (Type "done" To quit):""").title()

                if Add.lower() == "done":
                    print()
                    break
                elif Add == "":
                    print()
                    print("Please Select an Order")
                elif Menu.get(Add) is not None:
                    print()
                    Purchase.append(Add)

        elif Confirm.upper() == "Y":  # Confirmation of the Order
            return True


def process_payment(Total):
    while True:
        Cash = (input("Enter Your Cash Amount: ₱ "))  # Enter cash Of user

        if not Cash.isdigit():
            print()
            print("Please Enter A number:")
            continue

        Cash = int(Cash)  # Convert Cash Into Integer

        if Cash < Total:  # If user's money is insufficient, it resets.
            print()
            print("You Don't Have Enough Money For The Purchase. Please Try Again")
        elif Cash >= Total:  # If user's money is sufficient, it is done.
            Cash -= Total
            print()
            print(f"You Have A Change of: ₱{Cash:.2f}")
            print()
            print(f"Thank You For Dining at Mark Daniel's")
            print()
            break


def main():
    display_menu(Menu)
    take_order(Menu, Purchase)
    Total = calculate_total(Purchase, Menu)
    if confirm_order(Purchase, Menu, Total):
        print()
        print(f"Your Purchase Total Would be: ₱{Total}")  # Price total of all orders
        process_payment(Total)


main()
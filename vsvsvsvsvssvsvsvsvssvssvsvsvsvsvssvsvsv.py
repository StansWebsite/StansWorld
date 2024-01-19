# 2D list to hold table orders
tables = [
    ["TABLE 1 - ", 0], ["TABLE 2 - ", 0], ["TABLE 3 - ", 0], ["TABLE 4 - ", 0], ["TABLE 5 - ", 0],
    ["TABLE 6 - ", 0], ["TABLE 7 - ", 0], ["TABLE 8 - ", 0], ["TABLE 9 - ", 0], ["TABLE 10 - ", 0]
]

# Menu items stored as a dictionary
menu = {
    "Nachos": 5.50, "Soup": 4.95,
    "Burger": 10.50, "Brisket": 12.50, "Ribs": 15.00,
    "Corn": 2.50, "Fries": 3.00, "Salad": 3.25
}

# Function to get the server's name
def get_server_name():
    while True:
        server_name = input('Please enter your name: ')
        if server_name.isalpha():
            return "Server name: {}".format(server_name.capitalize())
        else:
            print("Sorry, you have not entered a recognized name.")

# Function to get the table number
def get_table_num():
    while True:
        table_num = input('Enter table number: ')
        if table_num.isdigit():
            table_num = int(table_num)
            if 1 <= table_num <= 10:
                return table_num
            else:
                print("Table number must be between 1 and 10")
        else:
            print("Sorry, you did not enter a table number")

# Function to get the menu item
def get_menu_item():
    while True:
        menu_item = input('Enter menu item. Type X if there are no more items to enter: ').capitalize()
        if menu_item == "X":
            return "X"
        elif menu_item in menu:
            return menu_item
        else:
            print("Sorry, you have not entered a valid menu item.")

# Function to get the quantity of an item
def get_qty():
    while True:
        qty = input('Enter quantity of the item required: ')
        if qty.isdigit():
            qty = int(qty)
            if qty > 0:
                return qty
            else:
                print("Quantity must be a positive number")
        else:
            print("Sorry, quantity must be a whole number")

# Function to get the discount choice
def get_discount_choice():
    while True:
        print("###############################################")
        print("######### Please choose a discount #########")
        print('## 1. Early Bird: Monday - Friday 5pm-7pm')
        print("## 2. Staff")
        print("## 3. No discount")
        print("")

        discount_choice = input("Select a discount to apply: ")
        if discount_choice.isdigit():
            discount_choice = int(discount_choice)
            if discount_choice in [1, 2, 3]:
                if discount_choice == 1:
                    return 15
                elif discount_choice == 2:
                    return 25
                else:
                    return 0
            else:
                print("Discount option must be 1, 2, or 3 only")
        else:
            print("Sorry, you did not enter a valid option")

# Main logic
enter_order = True

while enter_order:
    print("###############################################")
    print("#### Gurreb's BBQ order processing system  ####")
    print("###############################################")
    print("")
    print("############# Choose an option ################")
    print("")
    print("1. Enter customer order")
    print("2. Output bill")
    print("3. Exit")
    print("")

    main_choice = input('Enter option here: ')

    if main_choice == "1":
        server_name = get_server_name()
        table_num = get_table_num()
        tables[table_num - 1][0] = server_name
        tables[table_num - 1][1] = []
        subtotal = 0

        while True:
            item_choice = get_menu_item()

            if item_choice == "X":
                tables[table_num - 1][1].append(subtotal)
                break
            else:
                quantity = get_qty()
                price = menu[item_choice]
                cost = price * quantity
                tables[table_num - 1][1].extend([item_choice, quantity, cost])
                subtotal += cost

    elif main_choice == "2":
        table_num = get_table_num()
        discount = get_discount_choice()

        print(str(tables[table_num - 1][0]))
        print("Summary of bill before discounts:")
        print(str(tables[table_num - 1][1]))
        print("Discount percentage applied to this bill = {} ".format(discount))

        subtotal = sum(tables[table_num - 1][1][2::3])
        print("Subtotal before discount = £{}".format(subtotal))
        final_total = subtotal - (subtotal * (discount / 100))
        print("Final total after discount = £{}".format(final_total))

    elif main_choice == "3":
        break
    
    else:
        print("Please enter a valid option")

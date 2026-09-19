print("=========================")
print("   WELCOME TO CANTEEN    ")
print("=========================")
total_amount=0
total_items=0
bill_details= ""
n=int(input("how many items do you want to order? "))
for i in range(n):
    print("\n=====CATEGORIES=====")
    print("1. Tiffin")
    print("2. Lunch")
    print("3. Snacks")
    print("4. Drinks")
    print("======================")
    category_choice=int(input("enter category:"))
    match category_choice:
        case 1:
            category = "Tiffin"
            print("\n-----TIFFIN MENU-----")
            print("1. Idly  - ₹30")
            print("2. Vada  - ₹25")
            print("3. Dosa  - ₹40")
            print("4. Puri  - ₹45")
            choice=int(input("Enter your choice: "))
            match choice: 
                case 1:
                    item = "Idly"
                    price = 30
                case 2:
                    item = "Vada"
                    price = 25
                case 3:
                    item = "Dosa"
                    price = 40
                case 4:
                    item = "Puri"
                    price = 45
        case 2:
            category = "Lunch"
            print("\n------- LUNCH MENU -------")
            print("1. Meals       - ₹80")
            print("2. Biryani     - ₹120")
            print("3. Fried Rice  - ₹100")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    item = "Meals"
                    price = 80
                case 2:
                    item = "Biryani"
                    price = 120
                case 3:
                    item = "Fried Rice"
                    price = 100
                case _:
                    print("Invalid choice!")
                    continue
        case 3:
            category = "Snacks"
            print("\n------- SNACKS MENU -------")
            print("1. Samosa    - ₹15")
            print("2. Puffs     - ₹25")
            print("3. Biscuits  - ₹10")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    item = "Samosa"
                    price = 15
                case 2:
                    item = "Puffs"
                    price = 25
                case 3:
                    item = "Biscuits"
                    price = 10
                case _:
                    print("Invalid choice!")
                    continue
        case 4:
            category = "Drinks"
            print("\n------- DRINKS MENU -------")
            print("1. Tea         - ₹10")
            print("2. Coffee      - ₹20")
            print("3. Cool Drink  - ₹40")
            print("4. Water       - ₹20")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    item = "Tea"
                    price = 10
                case 2:
                    item = "Coffee"
                    price = 20
                case 3:
                    item = "Cool Drink"
                    price = 40
                case 4:
                    item = "Water"
                    price = 20
                case _:
                    print("Invalid choice!")
                    continue
        case _:
            print("Invalid category!")
            continue
    quantity = int(input("Enter quantity: "))
    amount = price * quantity
    bill_details += (
        f"{category:<12}"
        f"{item:<15}"
        f"{price:<8}"
        f"{quantity:<6}"
        f"{amount}\n"
    )
    total_amount += amount
    total_items += quantity
    print(f"{item} added successfully!")
    print(f"Amount: ₹{amount}")
print("\n============================================")
print("                 CANTEEN BILL                 ")
print("==============================================")
print(
    f"{'Category':<12}"
    f"{'Item':<15}"
    f"{'Price':<8}"
    f"{'Qty':<6}"
    f"{'Amount'}"
)
print("----------------------------------------------")
print(bill_details, end="")
print("----------------------------------------------")
print(f"Total Items  : {total_items}")
print(f"Total Amount : ₹{total_amount}")
print("==============================================")
print("          THANK YOU! VISIT AGAIN")
print("==============================================")
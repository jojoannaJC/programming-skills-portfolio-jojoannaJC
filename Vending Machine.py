#vending machine intro

print(""" 
───░█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▄ █▀▀█ █ █▀▀ 　 ░█──░█ █▀▀ █▀▀▄ █▀▀▄ ─▀─ █▀▀▄ █▀▀▀ 　 ░█▀▄▀█ █▀▀█ █▀▀ █──█ ─▀─ █▀▀▄ █▀▀ 
─▄─░█ █──█ █▄▄█ █──█ █──█ █▄▄█ ─ ▀▀█ 　 ─░█░█─ █▀▀ █──█ █──█ ▀█▀ █──█ █─▀█ 　 ░█░█░█ █▄▄█ █── █▀▀█ ▀█▀ █──█ █▀▀ 
░█▄▄█ ▀▀▀▀ ▀──▀ ▀──▀ ▀──▀ ▀──▀ ─ ▀▀▀ 　 ──▀▄▀─ ▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ░█──░█ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀""")
print("")
print("------------------------------------------------------------------------------")
print("----------------------Welcome to my Vending Machine!-------------------------")
print("--------Choose from our vast variety of snacks, drinks and many more!---------")
print("------------------------------------------------------------------------------")
print("")

#cold drinks menu

cold_drinks=[
    {"item_code": "A1",
     "item_name": "Iced Latte",
     "item_stock": 15,
     "item_price": 15},

     {"item_code": "A2",
     "item_name": "Iced Mocha",
     "item_stock": 15,
     "item_price": 15},
     
     {"item_code": "A3",
     "item_name": "Iced Vanilla Mocha",
     "item_stock": 12,
     "item_price": 15},

     {"item_code": "A4",
     "item_name": "Iced Peach Tea",
     "item_stock": 15,
     "item_price": 15},

     {"item_code": "A5",
     "item_name": "Iced Caramel Macchiato",
     "item_stock": 15,
     "item_price": 15},

     {"item_code": "A6",
     "item_name": "Iced Lemon Tea",
     "item_stock": 15,
     "item_price": 15},

]

#hot drinks menu

hot_drinks=[
    {"item_code": "B1",
     "item_name": "Cappuccino",
     "item_stock": 15,
     "item_price": 15},

     {"item_code": "B2",
     "item_name": "Latte",
     "item_stock": 15,
     "item_price": 15},

     {"item_code": "B3",
     "item_name": "Green Tea",
     "item_stock": 15,
     "item_price": 15},

     {"item_code": "B3",
     "item_name": "Espresso",
     "item_stock": 15,
     "item_price": 15},

     {"item_code": "B4",
     "item_name": "Chai",
     "item_stock": 15,
     "item_price": 15},

      {"item_code": "B5",
     "item_name": "Hot Chocolate",
     "item_stock": 10,
     "item_price": 15},
]



print("CODE | NAME | STOCK | PRICE")
print("")



#Chips menu

chips=[
    {"item_code": "C1",
     "item_name": "Lays",
     "item_stock": 20,
     "item_price": 7},

     {"item_code": "C2",
     "item_name": "Pringles",
     "item_stock": 20,
     "item_price": 7},

     {"item_code": "C3",
     "item_name": "Kurkure",
     "item_stock": 20,
     "item_price": 7},

     {"item_code": "C4",
     "item_name": "Cheetos",
     "item_stock": 20,
     "item_price": 7},

     {"item_code": "C5",
     "item_name": "Doritos",
     "item_stock": 20,
     "item_price": 7},

     {"item_code": "C6",
     "item_name": "Takis",
     "item_stock": 10,
     "item_price": 7},
]

#snacks menu

snacks=[
    {"item_code": "D1",
     "item_name": "Biscuits",
     "item_stock": 20,
     "item_price": 10},

     {"item_code": "D2",
     "item_name": "Cookies",
     "item_stock": 20,
     "item_price": 15},

     {"item_code": "D3",
     "item_name": "Croissants",
     "item_stock": 20,
     "item_price": 5},

     {"item_code": "D4",
     "item_name": "Popcorn",
     "item_stock": 20,
     "item_price": 5},

     {"item_code": "D5",
     "item_name": "Mixed nuts",
     "item_stock": 20,
     "item_price": 5}
]


#Kids menu

kids=[
    {"item_code": "E1",
     "item_name": "Fruit juice",
     "item_stock": 20,
     "item_price": 6},

     {"item_code": "E2",
     "item_name": "Oreos",
     "item_stock": 20,
     "item_price": 6},

     {"item_code": "E3",
     "item_name": "Gummy Bears",
     "item_stock": 20,
     "item_price": 6},

     {"item_code": "E4",
     "item_name": "Candy",
     "item_stock": 20,
     "item_price": 6},

     {"item_code": "E5",
     "item_name": "Chocalate Milk",
     "item_stock": 20,
     "item_price": 6},
]


def print_menu():
        print("----------Cold drinks menu---------- ")
        print("CODE | NAME | STOCK | PRICE")
        for item_data in cold_drinks: 
            print(item_data['item_code'],("|"), item_data['item_name'],("|"), item_data['item_stock'],("|"), item_data['item_price'])
        print("")
        print("----------Hot Drinks menu---------- ")
        print("CODE | NAME | STOCK | PRICE")
        for item_data in hot_drinks: 
            print(item_data['item_code'],("|"), item_data['item_name'],("|"), item_data['item_stock'],("|"), item_data['item_price'])
        print("")
        print("----------Chips menu---------- ")
        print("CODE | NAME | STOCK | PRICE")
        for item_data in chips: 
            print(item_data['item_code'],("|"), item_data['item_name'],("|"), item_data['item_stock'],("|"), item_data['item_price'])
        print("")
        print("----------Snacks menu---------- ")
        print("CODE | NAME | STOCK | PRICE")
        for item_data in snacks: 
            print(item_data['item_code'],("|"), item_data['item_name'],("|"), item_data['item_stock'],("|"), item_data['item_price'])
        print("")
        print("----------Kids menu---------- ")
        print("CODE | NAME | STOCK | PRICE")
        for item_data in kids: 
            print(item_data['item_code'],("|"), item_data['item_name'],("|"), item_data['item_stock'],("|"), item_data['item_price'])
        print("")

print_menu()


#calculating total price

money=(int(input("Enter amount: ")))
print("The entered amount is $",money)

user_input=str(input("Enter the item code: "))
#user_input = "D2"

#for selecting items in cold drinks menu 
def item_choice_cold_drinks():
    global money
    for item_data in cold_drinks:
        item_code = item_data['item_code']
        while user_input in item_code:
            item_name = item_data['item_name']
            print(f"You have selected {item_name}")
            item_price= item_data["item_price"]
            change = money-item_price
            money = change
            print(f"Your change is $ {change}")
            break 

item_choice_cold_drinks()

#for selecting items in hot drinks menu 
def item_choice_hot_drinks():
    for item_data in hot_drinks:
        item_code = item_data['item_code']
        while user_input in item_code:
            item_name = item_data['item_name']
            print(f"You have selected {item_name}")
            item_price= item_data["item_price"]
            change = money-item_price
            money = change
            print(f"Your change is $ {change}")
            break
item_choice_hot_drinks()
        
#for selecting items in chips menu 
def item_choice_chips():
    for item_data in chips:
        item_code = item_data['item_code']
        while user_input in item_code:
            item_name = item_data['item_name']
            print(f"You have selected {item_name}")
            item_price= item_data["item_price"]
            change = money-item_price
            money = change
            print(f"Your change is $ {change}")
            break
item_choice_chips()

#for selecting items in snacks menu
def item_choice_snacks():
    for item_data in snacks:
        item_code = item_data['item_code']
        while user_input in item_code:
            item_name = item_data['item_name']
            print(f"You have selected {item_name}")
            item_price= item_data["item_price"]
            change = money-item_price
            money = change
            print(f"Your change is $ {change}")
            break
item_choice_snacks()


#for selecting items in kids menu 
def item_choice_kids():
    for item_data in kids:
        item_code = item_data['item_code']
        while user_input in item_code:
            item_name = item_data['item_name']
            print(f"You have selected {item_name}")
            item_price= item_data["item_price"]
            change = money-item_price
            money = change
            print(f"Your change is $ {change}")
            break

item_choice_kids()

print("Your item has been dispensed!")
print("")

#recommendations list for cold drinks:

if user_input=="A1":
    print("This Item would go well with some snacks. Would you like to purchase them?")
if user_input=="A2":
    print("This Item would go well with some snacks. Would you like to purchase them?")
if user_input=="A3":
    print("This Item would go well with some snacks. Would you like to purchase them?")
if user_input=="A4":
    print("This Item would go well with some snacks. Would you like to purchase them?")
if user_input=="A5":
    print("This Item would go well with some snacks. Would you like to purchase them?")

#recommendations list for Hot drinks:

if user_input=="B1":
    print("This Item would go well with some snacks. Would you like to purchase them?")
if user_input=="B2":
    print("This Item would go well with some snacks. Would you like to purchase them?")
if user_input=="B3":
    print("This Item would go well with some snacks. Would you like to purchase them?")
if user_input=="B4":
    print("This Item would go well with some snacks. Would you like to purchase them?")
if user_input=="B5":
    print("This Item would go well with some snacks. Would you like to purchase them?")

#recommendations list for Chips:

if user_input=="C1":
    print("This Item would go well with some drinks. Would you like to purchase them?")
if user_input=="C2":
    print("This Item would go well with some drinks. Would you like to purchase them?")
if user_input=="C3":
    print("This Item would go well with some drinks. Would you like to purchase them?")
if user_input=="C4":
    print("This Item would go well with some drinks. Would you like to purchase them?")
if user_input=="C5":
    print("This Item would go well with some drinks. Would you like to purchase them?")


#recommendations list for snacks:

if user_input=="C1":
    print("This Item would go well with some drinks. Would you like to purchase them?")
if user_input=="C2":
    print("This Item would go well with some drinks. Would you like to purchase them?")
if user_input=="C3":
    print("This Item would go well with some drinks. Would you like to purchase them?")
if user_input=="C4":
    print("This Item would go well with some drinks. Would you like to purchase them?")
if user_input=="C5":
    print("This Item would go well with some drinks. Would you like to purchase them?")

#asking user to buy more items

users_inputs= input("Would you like to buy more items with your purchase? (Yes/No): ")

#if yes:

if users_inputs =="Yes":
    user_input= str("Enter Item code: ")
    item_choice_cold_drinks()
    item_choice_hot_drinks()
    item_choice_chips()
    item_choice_snacks()
    item_choice_kids()

if users_inputs =="No":
    print("Thank you for purchasing with us!")
    print("Have a great day!")


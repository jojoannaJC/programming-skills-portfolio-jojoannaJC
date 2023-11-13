#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
#As they enter each topping, print a message saying you’ll add that topping to their pizza.


while True:
    pizza=input("What toppings would you like on your pizza? ")
    if pizza== "quit":
        break
    print("The toppings have been added.")

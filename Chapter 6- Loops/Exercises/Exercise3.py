#Write a loop that never ends, and run it. 
#(To end the loop, press ctrl-C or close the window displaying the output.)

while True:
    age=input("Enter your current age: ")

    age=int(age)

    if age < 3: 
        print("You are very young!")
    elif age < 40: 
        print("You are young.")
    else:
        print("You are old.")
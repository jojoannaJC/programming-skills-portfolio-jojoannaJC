#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
#If the alien is green, print a message that the player earned 5 points.
#If the alien is yellow, print a message that the player earned 10 points.
#If the alien is red, print a message that the player earned 15 points.
#Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color=("red")
ac=(input("What is the alien's color?: "))
if ac=="green":
    print("5 points earned!!")

elif alien_color=="yellow":
    print("10 points earned!!")

else:
    print("15 points earned!!")


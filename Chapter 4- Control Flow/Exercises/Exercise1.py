#Imagine an alien was just shot down in a game. 
#Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)


#passed version
alien_color=("green")
ac=(input("What is the alien's color?: "))
if ac=="green":
    print("5 points earned!!")
else:
    print("0 points")

#fail version
alien_color=("red")
ac=(input("What is the alien's color?: "))
if ac=="green":
    print("5 points earned!!")
else:
    print("0 points")
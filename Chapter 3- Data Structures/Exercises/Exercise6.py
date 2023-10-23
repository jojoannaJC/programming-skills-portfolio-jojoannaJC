#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#Use pop() to remove guests from your list one at a time until only two names remain in your list. 
#Each time you pop a name from your list, print a message to that person to let them know you’re sorry you can’t invite them.
#Print a message to each of the two people still on your list, letting them know they’re still invited.
#Use del to remove the last two names from your list, so you have an empty list. 
#Print your list to make sure you actually have an empty list at the end of your program.

ilist=["Luka Coffaine", "Roronoa Zoro", "Portugas D. Ace", "Edgar Allan Poe", "Joanna Christabel"]

ilist[1]="Michelangelo"

print("""Hello Everyone. Due to certain circumstances, we have unfortunately shortened the guest list.
      We are deeply sorry for the inconviences caused and we hope you accept our sincerest apologies.""")

print("We shall send out the updated invite list soon.")
print("")

name=ilist.pop()
print("Sorry " + name.title(), "You are no longer invited to the dinner party.")

name=ilist.pop()
print("Sorry " + name.title(), "You are no longer invited to the dinner party.")

name=ilist.pop()
print("Sorry " + name.title(), "You are no longer invited to the dinner party.")
print("")

name=ilist[0].title()
print(name+ ", You are still on the invite list and we hope to see you at the dinner party.")

name=ilist[1].title()
print(name+ ", You are still on the invite list and we hope to see you at the dinner party.")






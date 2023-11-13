#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#* Think of five programming words you’ve learned about in the previous chapters. 
#Use these words as the keys in your glossary, and store their meanings as values.
#* Print each word and its meaning as neatly formatted output. 
#You might print the word followed by a colon and then its meaning, 
#or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

g={
    "string": "series of characters",
    "dictionary": "collection of key values",
    "list": "olderly collection of data",
    "comment": "lines in the code ignored by the computer",
    "loop": "collection of items displayed one at a time"
}

mean="string"
print("\n" + mean.title() + ": " + g[mean])

mean="dictionary"
print("\n" + mean.title() + ": " + g[mean])

mean="list"
print("\n" + mean.title() + ": " + g[mean])

mean="comment"
print("\n" + mean.title() + ": " + g[mean])

mean="loop"
print("\n" + mean.title() + ": " + g[mean])

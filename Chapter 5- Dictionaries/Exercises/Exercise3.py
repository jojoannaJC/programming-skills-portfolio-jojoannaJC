#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. 
#When you’re sure that your loop works, add five more Python terms to your glossary.
#When you run your program again, these new words and meanings should automatically be included in the output.

g={
    "string": "series of characters",
    "dictionary": "collection of key values",
    "list": "olderly collection of data",
    "comment": "lines in the code ignored by the computer",
    "loop": "collection of items displayed one at a time",
    "int": "integer number type",
    "float": "integer value with decimal",
    "boolean": "true or false expression function",
    "value": "item associated with key/dictionary",
    "key": "first value in a dictionary"
}

for word, definition in g.items():
    print("\n" + word.title() + ":" + definition)
#Make a dictionary containing three major rivers and the country each river runs through. 
#One key-value pair might be 'nile': 'egypt'.

#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

#* Use a loop to print the name of each river included in the dictionary.

#* Use a loop to print the name of each country included in the dictionary.

rivers= {
    "Ganga": "India", 
    "Nile": "Egypt",
    "Amazon": "South America"
}

for river, country in rivers.items():
    print("The river" + river.title()+ "flows through " + country.title() + ".")

print("n\The rivers included are: ") 
for river in rivers.keys():
    print("- " + river.title())

print("n\The countries included are: ") 
for country in rivers.keys():
    print("- " + country.title())






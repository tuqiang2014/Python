tabby_cat = "\tT'm tabbed in."
persian_cat = "I'm spilt\non a line."
backslash_cat = "I'm \\ a\\ cat."

fat_cat = """
I'll do a list；
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Gtass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

while True:
    for i in ["/","-","|","\\","|"]:
	    print("%s\r" % i,)
#problem1: SyntaxError: EOL while scanning string literal

#input("why no quotes)
 #error message File "answers1.py", line 1
#input("why no quotes)
      #^
      #SyntaxError: EOL while scanning string literal
#The EOL error code means pyhton hit the end of a line going through a string because either the quotation marks were
#forgotten at the end or beginning.

#problem2:

x = ["apple", "banana", "carrot"]
print("apple"+'s ' + "banana" +'s and ' + "carrot" + 's')
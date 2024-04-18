#Emanuele Giacomozzi
#17/04/2023
'''
2-3. Personal Message: Use a variable to represent a person’s name, 
and print a message to that person. 
Your message should be simple, such as,
“Hello Eric, would you like to learn some Python today?”
'''

Name:str = "Emanuele"
print(f"Hello {Name}, would you like to learn some python today?")

'''
2-4. Name Cases: Use a variable to represent a person’s name,
 and then print that person’s name in lowercase, uppercase, 
 and title case.
'''

name:str = "Emanuele"
name_lower:str = name.lower()
name_upper:str = name.upper()
name_title:str = name.title()
print(name_lower, name_upper, name_title)

'''
2-5. Famous Quote: Find a quote from a famous person you admire. 
Print the quote and the name of its author. 
Your output should look something like the following,
including the quotation marks: Albert Einstein once said,
“A person who never made a mistake never tried anything new.”
'''
quote:str = "Forza Roma"
famous_person:str = "Francesco Totti"
print(f"{famous_person} once said \"{quote}\" ")

'''
2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
Assign the value 'python_notes.txt' to a variable called filename.
 Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
'''
filename:str = "python_notes.txt"
print(filename.removesuffix('.txt'))

'''
3-1. Names: Store the names of a few of your friends in a list called names.
 Print each person’s name by accessing each element in the list, one at a time.
'''
Names = ["Giorgio", "Mario", "Simone", "Carlo"]
for i in Names:
    print(i)

'''
3-2. Greetings: Start with the list you used in Exercise 3-1,
 but instead of just printing each person’s name, print a message to them. 
The text of each message should be the same, but each message should be personalized with the person’s name.
'''
Names = ["Giorgio", "Mario", "Simone", "Carlo"]
message = "come stai?"
for i in Names:
    print(f"{i} {message}")

'''
3-3. Your Own List: Think of your favorite mode of transportation,
 such as a motorcycle or a car, and make a list that stores several examples. 
 Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.
'''

mezzo_trasporto:list = ["motocicletta", "panda", "autobus"]
print(f"Vorrei comprare una {mezzo_trasporto[0]}, ma guido una {mezzo_trasporto[1]}, perché non voglio prendere l'{mezzo_trasporto[2]}")

'''
3-4. Guest List: If you could invite anyone, living or deceased,
 to dinner, who would you invite? Make a list that includes at 
 least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
'''

guest:list = ["Pino", "Franco", "Gianluca"]
print(f"Ciao {guest[0]} vuoi venire a cena?")
print(f"Ciao {guest[1]} vuoi venire a cena?")
print(f"Ciao {guest[2]} vuoi venire a cena?")









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
Names:list = ["Giorgio", "Mario", "Simone", "Carlo"]
for i in Names:
    print(i)

'''
3-2. Greetings: Start with the list you used in Exercise 3-1,
 but instead of just printing each person’s name, print a message to them. 
The text of each message should be the same, but each message should be personalized with the person’s name.
'''
Names:list = ["Giorgio", "Mario", "Simone", "Carlo"]
message:str = "come stai?"
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

'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
'''
guest:list = ["Pino", "Franco", "Gianluca"]
print(f"{guest[2]} non potrà partecipare")
guest[2] = "Marco"
for i in guest:
    print(f"Ciao {i} , vuoi venire a cena?")

'''
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''
guest:list = ["Pino", "Franco", "Gianluca"]
print("Ho trovato una sala più grande")
guest.insert(0, "Gianni")
guest.insert(2, "Maria")
guest.append("Sofia")
for i in guest:
    print(f"Ciao {i} , vuoi venire a cena?")

'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
'''

guest:list = ["Pino", "Franco", "Gianluca"]
print("Ho trovato una sala più grande")
guest.insert(0, "Gianni")
guest.insert(2, "Maria")
guest.append("Sofia")
for i in guest:
    print(f"Ciao {i} , vuoi venire a cena?")
print(f"Ciao mi dispiace ma posso invitare solo due persone")
print(f"Ciao {guest[0]}, mi dispiace ma non posso più invitarti")
guest.pop(0)
print(f"Ciao {guest[1]}, mi dispiace ma non posso più invitarti")
guest.pop(1)
print(f"Ciao {guest[1]}, mi dispiace ma non posso più invitarti")
guest.pop(1)
print(f"Ciao {guest[1]}, mi dispiace ma non posso più invitarti")
guest.pop(1)
for i in guest:
    print(f"Ciao {i} sei uno dei due invitati rimasti")
del guest[0]
del guest[0]
print(guest)

'''
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
'''

places:list = ["Los Angeles", "Dublino", "Polinesia", "Tokyo", "Rio de Janeiro"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(sorted(places, reverse=False))
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)

'''
3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
use len() to print a message indicating the number of people you’re inviting to dinner.
'''

guest:list = ["Pino", "Franco", "Gianluca"]
print("Ho trovato una sala più grande")
guest.insert(0, "Gianni")
guest.insert(2, "Maria")
guest.append("Sofia")
print("Quanti sono gli invitati: ", len(guest))

'''
3-10. Every Function: Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
'''

seriea_teams:list = ["Inter", "Milan", "Juventus", "Bologna", "Roma", "Atalanta", "Lazio", "Napoli", "Fiorentina", "Monza", "Torino", "Genoa", "Empoli", "Cagliari", "Udinese", "Lecce", "H.Verona", "Frosinone", "Sassuolo", "Salernitana"]
print("In Serie A ci sono : ", len(seriea_teams), " squadre")
print(f"La capolista della Serie A è l'{seriea_teams[0].upper()}, l'ultima squadra della Serie A è la {seriea_teams[-1].lower()}")
print("La mia squadra del cuore è: ", seriea_teams[4].title())
serieb_teams:list = ["Parma", "Venezia", "Cremonese"]
print(f"Queste sono le prime squadre di Serie B che saliranno in Serie A : {serieb_teams} ")
print(f"Queste sono le ultime squadre di Serie A che scenderanno in Serie B : {seriea_teams[-3:]} ")
seriea_teams.pop(-3)
seriea_teams.pop(-2)
seriea_teams.pop(-1)
print(seriea_teams)
seriea_teams.append(serieb_teams[0])
seriea_teams.insert(-1, serieb_teams[1])
seriea_teams.append(serieb_teams[2])
print(sorted(seriea_teams))
print(sorted(seriea_teams, reverse=True))
print(sorted(seriea_teams, reverse=False))
print(seriea_teams)
seriea_teams.sort()
print(seriea_teams)
seriea_teams.sort(reverse = True)
print(seriea_teams)
del[serieb_teams[0:]]
print(serieb_teams)
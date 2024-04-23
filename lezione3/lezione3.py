'''
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
'''

def pizza_type(pizza:list):
    for elem in pizza:
        print(f"Mi piace la pizza {elem}")
    print("Adoro la pizza")
    return pizza
pizza:list = ["Margherita", "Capricciosa", "Pistacchiosa"]
pizza_type(pizza)

'''
4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!
'''

def animal_type(animal:list): #i use a function called animal_type that return the animals list
    for elem in animal:
        if elem == "Elephant":
            print(f"The {animal[0]} has fangs") #if the animal in list is the elephant, print this message
        elif elem == "Giraffe":
            print(f"The {animal[1]} has a long neck") #if the animal is the giraffe, print this message
        else:
            print(f"The {animal[2]} lives in the seas") #else print this message
    print("Each of these animals is very big")
    return elem 
animal:list = ["Elephant", "Giraffe", "Whale"]
animal_type(animal)

'''
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
'''

numbers:int = range(1,21)
for n in numbers:
    print(n)

'''
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
'''
n:int = 1 #i've initialized a variable n and i've assigned the value 1
n1:int = 1000001 #i've initialized a variable n1 and i've assigned the value 1000001 because the range is from 1 to 1000000 inclusive
numbers:list = list(range(n,n1)) #'i've make a list which has as range n(1), n1(1000000)
print(numbers)

'''
4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
'''


numbers:list = list(range(1,1000001))
min_number:int = min(numbers)
print(min_number)
max_number:int = max(numbers)
print(max_number)
sum_numbers:int = sum(numbers)


 

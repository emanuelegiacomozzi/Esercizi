'''
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
'''

def pizza_type(pizza:list):
    for elem in pizza:
        print(f"I like the {elem} pizza")
    print("I love pizza")
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
n1:int = 10 #i've initialized a variable n1 and i've assigned the value 1000001 because the range is from 1 to 1000000 inclusive
numbers:list = list(range(n,n1)) #'i've make a list which has as range n(1), n1(1000000)
print(numbers)

'''
4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
'''


numbers:list = list(range(1,10))
min_number:int = min(numbers)
print(min_number)
max_number:int = max(numbers)
print(max_number)
sum_numbers:int = sum(numbers)
print(sum_numbers)

'''
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
'''

odd:list = list(range(1,21,2))
for n in odd:
    print(n)

'''
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
'''
multiples:list = list(range(3,31,3))
for n in multiples:
    print(n)

'''
4-8. Cubes: A number raised to the third power is called a cube. 
For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
'''
cubes:list = list(range(1,11))
for cube in cubes:
    print(cube**3)

'''
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
'''
cubes:list = list(range(1,11))
cubes1:list = [cube**3 for cube in cubes]
print(cubes1 )

'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
'''
cubes:list = list(range(1,11))
cubes1:list = [cube**3 for cube in cubes]
print(cubes1)
print(len(cubes1)) #i control the lenght of the list cubes1 
print("The first three elements are: ",cubes1[0:3]) #print the first three elements
print("The last three elements are: ",cubes1[-3:]) #prints the last three elements
central_index1:int = len(cubes1) // 2 #calculate the index of the centre of the cubes1 list
central_index2:int = len(cubes1) // 2 - 1 #calculate the index preceding the centre index 
central_index3:int = len(cubes1) // 2 + 1 #calculate the index following the centre index 
print("The three central element are: ", cubes1[central_index2],cubes1[central_index1],cubes1[central_index3])

'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list
'''
def pizza_type(pizza:list):
    for elem in pizza:
        print(f"I like the {elem} pizza")
    print("I love pizza")
    return pizza
pizza:list = ["Margherita", "Capricciosa", "Pistacchiosa"]
pizza_type(pizza)
friend_pizzas:list = pizza.copy() #i've create a copy of pizza list
pizza.append("Diavola")
friend_pizzas.append("Marinara")
my_pizzas:list = [elem for elem in pizza] #i've use the list comprehension to print the list
friend_pizzas1:list = [elem for elem in friend_pizzas]
print("My favorite pizzas are: ", my_pizzas)
print("Your favorite pizzas are: ", friend_pizzas1)

'''
4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
'''

'''
4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008. You won’t use much of it now, but it might be interesting to skim through it.
'''

'''
4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.
'''
#first
cubes:list = list(range(1,11))
cubes1:list = [cube**3 for cube in cubes]
print(cubes1)
print(len(cubes1)) #i control the lenght of the list cubes1 
print("The first three elements are: ",cubes1[0:3]) #print the first three elements
print("The last three elements are: ",cubes1[-3:]) #prints the last three elements
central_index1:int = len(cubes1) // 2 #calculate the index of the centre of the cubes1 list
central_index2:int = len(cubes1) // 2-1 #calculate the index preceding the centre index 
central_index3:int = len(cubes1) // 2+1 #calculate the index following the centre index 
print("The three central element are: ", cubes1[central_index2],cubes1[central_index1],cubes1[central_index3])

#second
def pizza_type(pizza:list):
    for elem in pizza:
        print(f"I like the {elem} pizza")
    print("I love pizza")
    return pizza
pizza:list = ["Margherita", "Capricciosa", "Pistacchiosa"]
pizza_type(pizza)
friend_pizzas:list = pizza.copy() #i've create a copy of pizza list
pizza.append("Diavola")
friend_pizzas.append("Marinara")
my_pizzas:list = [elem for elem in pizza] #i've use the list comprehension to print the list
friend_pizzas1:list = [elem for elem in friend_pizzas]
print("My favorite pizzas are: ", my_pizzas)
print("Your favorite pizzas are: ", friend_pizzas1)

#third
numbers:list = list(range(1,10))
min_number:int = min(numbers)
print(min_number)
max_number:int = max(numbers)
print(max_number)
sum_numbers:int = sum(numbers)
print(sum_numbers)
 

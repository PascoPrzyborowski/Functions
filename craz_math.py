



# x = 3
# y= 4

# # sum = x + y

# # print(sum) 

# def sum(x, y):
#     return x + y

# x =3
# y =4
# print(sum(x, y))

# books = 10
# pens = 20
# #
# def sum1(pens, books):
#     return pens + books
# books = 10
# pens = 20

# sum1(books, pens)

# def coffee_maschine(beans_in_kg, water_in_liters):
#     print("You have ", beans_in_kg, "kgs. Water level: ", water_in_liters)
#     #return beans_in_kg + water_in_liters
#     total_cups = 120 * beans_in_kg
#     return total_cups


# target = 1000
# cups = coffee_maschine(1,4)
# rounds_target_value = target / cups
# print("need to run in Machine!", rounds_target_value)


# def coffee_machine(beans_in_kg, water_in_liters):
#     print("You have ", beans_in_kg, "kgs. Water level: ", water_in_liters)
#     # how many cups can we get with this input?  
#     # 1kg - 120 cups
#     total_cups = 120 * beans_in_kg
#     # return beans_in_kg + water_in_liters
#     return total_cups

# # Forget the sciece --> liters to kg! density? 


# # 1 euro per cup
# target = 1000
# # restaurant manager - has a target! 1000 euros per day
# # "reduce" -  stock of coffee, etc.
# # Formula! Correctness!! 
# # target / total_cups
# cups = coffee_machine(1, 4)
# rounds_to_make_target_value = target / cups
# print("You need to run this machine ", rounds_to_make_target_value)

# # Tasks

# # Addition
# # Substraction
# # Division
# # Multiplikation


# def add_it(num1, num2):
#     sum = num1 + num2
#     return sum

# def substract_it(num1, num2):
#     sub = num1 - num2
#     return sub

# def multiplic_it(num1, num2):
#     mul = num1 * num2
#     return mul

# def div_it(num1, num2):
#     if num2 == 0:
#         print("Can not divide by Zero!")
#         return
#     div = num1 / num2
#     return div
#     # try:
#     #     return num1 / num2
#     # except Zero_div:
#     #     print("Can not divide by Zero!")

# print()

# num1 =int(input("Give me a Number: "))
# num2 =int(input("Give me a Number: "))

# print()
# print("The summary of the Numbers", num1, "and", num2, "is: ",add_it(num1,num2))
# print()
# print("The substract of the Numbers", num1, "and", num2, "is: ",substract_it(num1,num2))
# print()
# print("The multiplication of the Numbers", num1, "and", num2, "is: ",multiplic_it(num1,num2))
# print()
# print("The division of the Numbers", num1, "and", num2, "is: ",div_it(num1,num2))
# print()



# x = [1,2,3,4]
# print()
# print(x)
# print()
# print(max(x))
# print()
# print(min(x))
# print()

#print(dir(__builtins__))
#help(type)

# def greet(name):
#     return f"Hello {name}"


# a_name = input("Give me a Name: ")

# store = greet(a_name)
# print(store)

# def greet(name =(input("Give me a Name: "))):
#     return f"Hello {name}"

# store = greet()
# print(store)

# def full_names(first_name, last_name):
#     return f"{first_name}, {last_name}"

# print(full_names('pasco', 'me_is'))

# def full_name(first_name="John", last_name="Doe"):
#     return f"Good Morning {first_name}{last_name}"

# print(full_name("Peter"))

# def greet(first_name="John ", last_name="Doe ", salutation="Dear Sir/Madam "):
#     return f"{salutation}{first_name}{last_name} you are invited"

# print(greet())

# def full_name(first_name, middle_name, religious_name, maritial_name, last_name):
#    return f"{first_name}, {middle_name}, {religious_name}, {maritial_name}, {last_name}"

def full_name(*args):#"list Tuple"
     print(args)
     #return f"{args[0]} {args[1]} {args[2]} {args[3]}"

print(full_name("Felipe", "Gonzales", "Pedro","Alfonso"))



#shoe_sizes = (3,4,5,6,7,) #Tuple not changed
shoe_sizes = [3,4,5,6,7,]   #list can be changed
print(shoe_sizes)
shoe_sizes.append(100)
print(shoe_sizes)
shoe_sizes.pop(5)
print(shoe_sizes)
shoe_sizes.remove(5)
print(shoe_sizes)
shoe_sizes.insert(1,"Gotcha!")
print(shoe_sizes)
shoe_sizes[index]=int(input("What shoe do u want"))
print(shoe_sizes)
print(shoe_sizes[0])
print(shoe_sizes[4])
print(shoe_sizes[-1])


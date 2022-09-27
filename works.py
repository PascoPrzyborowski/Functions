# greetings = {
#     "key": "value",
#     "table": "food on",
#     "car": "maschine to drive"
# }

#def hello(last_name = "doe", first_name = "jane"): pass  <-- no
#def Function (args!!, Kwargs!!):

# def full_name(*args,):
#     full_string = ""
#     for name in args:
#         full_string += name
#     return full_string

# def full_name2(*args,**kwargs,):
#     print(kwargs)
#     print(args)
#     first_name = kwargs["first_name"]
#     last_name = kwargs["last_name"]
#     return f"{first_name},{last_name}"



# print(full_name2(first_name='Jane', last_name='Doe'))

#print(full_name(first_name()))

# def full_name(*args, **kwargs): # kwargs are DICTIONARIES
#     print('--kwargs: ->', kwargs)
#     print('---args: ->', args)
#     first_name = kwargs["first_name"]
#     last_name = kwargs["last_name"]
#     return f"{args[0]} {first_name} {last_name}"

# # how to use it!
# print(full_name('Good morning', first_name='Jane', last_name='Doe', location="Berlin"))

# print()
# print(full_name(first_name(input)))


# first_name = "" #gobal var
# last_name = "Doe"
# def full_name():
#     first_name = "Peer" # local var , localscope
#     last_name = "Hoffmann"
#     print(first_name, 'first name')
#     print(last_name, 'last_name')
#     def add_sir(name):
#         return f"Sir {name} {last_name}"
#     new_full_name = add_sir(first_name)
#     #return f"{first_name} {last_name}"
#     return new_full_name

# print(full_name())

# print(first_name)
# print(last_name)
# first_name_out = "Jac"

# def full_name1():
#     first_name_in = "fausto"
#     #print(first_name_in)
#     return first_name_in

# #first_name = "Jac"
# print(full_name1())
# print(first_name_out)

# first_name_out = ["Jac"] #List

# def full_name1(first_name_out):
#     #first_name_out[0] = "fausto"
#     #print(first_name_in)
#     return first_name_out

# first_name = "Jac"
# full_name1(first_name_out)
# print(first_name_out)
# print(type(first_name_out))

# first_name_out = {"Jac",} #Dic

# def full_name1(first_name_out):
#     first_name_out{0,} = "fausto"
#     #print(first_name_in)
#     return first_name_out

#first_name = "Jac"
# full_name1(first_name_out)
# print(first_name_out)
# print(type(first_name_out))


# last_name = ["Doe"]
# # "Pass by reference" variables can change
# def full_name(last_name):
#     # variations 
#     last_name[0] = "Hoffmann"
#     return last_name

# full_name(last_name)
# print(last_name)

# last_name = {"last_name":"Doe"}
# # "Pass by reference" variables can change
# def full_name(last_name):
#     # variations 
#     last_name["last_name"] = "Hoffmann"
#     return last_name

# full_name(last_name)
# print(last_name)
# print(type(last_name))

import time
#passing by value ! Numbers and Strings

names = {"first_name":"Jullian","last_name":"Assange"} #init dict
time.sleep(1)
print("Original Dict:")
print()
print(names)
print()
print("Now changed with Function:")
print()
# "Pass by reference" variables can change
def full_name(last_name):
    # variations 
    names["first_name"] = input("enter a name: ") #add and rename item
    #names["first_name"] = "John" #add and rename item
    names["last_name"] = "Snowden" #add and rename item
    return names

full_name(names) # output
print(names)
print(type(names)) # type of 







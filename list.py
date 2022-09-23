# names = ["Victor", "Peter", "Mary", "John", "Badara", "Peer"]
# # 
# # using an index, replace "Peer" with "Malcom X"

# # Add two names to the list of names

# # Experiment with the methods in a list using dir(names)
# print()
# print(names)
# print()
# names[5]="Malcom y"
# print(names)
# print()
# names[-1]="Malcom x"
# print(names)
# print()
# index_of=names.index(names[-1])
# print(index_of)
# print()
# names.append("Hans")
# names.append("Wurst")
# names.append("Nadia")
# names.append("Emily")
# names.append("Peer")
# names.append("Fausto")
# names.append("P_Eminence")
# print(names)
# print()
# names.pop(6)
# print(names)
# print()
# names.remove("John")
# print(names)
# print()
# names.insert(1,"Gotcha!")
# print(names)
# print()
# index = names.index("Peer")
# names[index] = "Malcom X"
# names.append("Dimi")
# names.extend("Main")
# print(names)
# print(len(dir(list)))
# #print(dir(list))
# print()



# def full_name(*args):
    
#    # return f"{args[0], args[1],args[2],args[3],args[4],}"
#     return args

# full_name("X","jr", "jr", "jr", "jr", "jr", "jr", "jr", "jr", )
# #names = ['na','na','na','na','an']
# names = ('Felipe', 'Gonzales')  #[] list, ()tuple

# full_string = ""
# for name in names:
#     full_string += f"{name} " # name + " "
# #    print(name, end="")

# print(full_string.strip())

# #print(" ".join(names))

# def full_name(*args): # "tuple"
#     # 2 names, 3 etc.
#     # Handle it "gracefully!!"
#     # print(args)
#     # return f"{args[0]} {args[1]} {args[2]} {args[3]}"
#     # --> TUPLE / List (Tuples cannot be changed/mutated )
#     return args

# # looping crash
# names = ('Felipe', 'Gonzalez') ## tuple

# # 2 major ways of doing it
# full_string = ""
# for name in names:
#     full_string += f"{name} " # name + " " $$$
#     # print(name, end="") # A for effort!!!

# print(full_string.strip())  

# full_string = ""
# for name in names:
#     full_string += f"{name} " # name + " "


def full_name(*args): # "tuple"
    full_string = " "
    for name in args:
        full_string += f"{name}"
    return full_string


names = ('Felipe', 'Gonzales')

print(full_name("Felipe", "Gonzales", "Garcia", "Gonzales", "Garcia", "Gonzales","Garcia"))
print(full_name("Felipe", "Gonazales"))
print(full_name("Gonzales"))

#print(full_name("Felipe","B","C",))


    # 2 names, 3 etc.
    # Handle it "gracefully!!"
    # print(args)
    # return f"{args[0]} {args[1]} {args[2]} {args[3]}"
    # --> TUPLE / List (Tuples cannot be changed/mutated )
    # return args

# looping crash
# names = ('Felipe', 'Gonzalez') ## tuple

# # 2 major ways of doing it
# full_string = ""
# for name in names:
#     full_string += f"{name} " # name + " " $$$
#     # print(name, end="") # A for effort!!!

# print(full_string.strip())  


# # full_name("A", "B", "C");
# # full_name("A", "B");
# # full_name("A");



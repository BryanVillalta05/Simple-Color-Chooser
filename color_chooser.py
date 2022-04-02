import random
color_list=["black", "white", "red", "blue", "orange", "green", "brown", "gray", "light blue"]
print(color_list)
color=random.choice(color_list)
print(color)
selection=input("¿Desea otro color? y/n")
while selection != "n":
    if selection == "y":
        color_list.remove(color)
        color=random.choice(color_list)
        print(color)
        print(color_list)
        selection=input("¿Desea otro color? y/n")
print("Muchas gracias por usar el programa")

name = input("Your name: ")
x = input("How many pizzas you want? ")
y = input("How many pieces of pepperoni do you want?  ")
z = input("How many olives do you want? ")
print(name + " wants " + x + " pieces of the stupid pizzas, " + y + " pieces of pepperoni(s), and " + z + " gigantic olives.")
print("ThankYouComeAgain")
name2 = input("Your name: ")
x2 = input("How many pizzas you want? ")
y2 = input("How many pieces of pepperoni do you want?  ")
z2 = input("How many olives do you want? ")
print(name2 + " wants " + x2 + " pieces of the stupid pizzas, " + y2 + " pieces of pepperoni(s), and " + z2 + " gigantic olives.")
print("ThankYouComeAgain")
name3 = input("Your name: ")
x3 = input("How many pizzas you want? ")
y3 = input("How many pieces of pepperoni do you want?  ")
z3 = input("How many olives do you want? ")
print(name3 + " wants " + x3 + " pieces of the stupid pizzas, " + y3 + " pieces of pepperoni(s), and " + z3 + " gigantic olives.")
print("ThankYouComeAgain")
x = int(x)
x2 = int(x2)
x3 = int(x3)
y = int(y)
y2 = int(y2)
y3 = int(y3)
z = int(z)
z2 = int(z2)
z3 = int(z3)
print('''
Average:''')
print("Pizzas: " + str((float(x) + float(x2) + float(x3))/3))
print("Pepperonis: " + str((float(y) + float(y2) + float(y3))/3))
print("Olives: " +str((float(z) + float(z2) + float(z3))/3))
#we're finally on OOP!
#seems like I skipped ahead a bit but that's just so I could
#take notes too

# import turtle

# timmy = turtle.Turtle()
# screen = turtle.Screen()

# timmy.shape("turtle")
# timmy.color("Magenta")

# for i in range(100):
#     timmy.forward(1)

# screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)
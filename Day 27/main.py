from milesToKmConverter import MilesToKmConverter
# Like varargs in C#
# the variable parameters declaration always has the asterisk followed by the name of the parameter collection
# in this case name.  So, in full, it's called *name
# def functionWithVariableParameters(*name):
#     for n in name:
#         print(n)

# functionWithVariableParameters("jonathan", "blackwell", "was", "here")

#you can even specify the type of the arguments
#all of the items come in as an n-long tuple
# def add(*numbers:int):
#     #arguments can be accessed by index
#     #numbers[0], numbers[14], etc
#     print(sum(numbers))

# add(1,2,3,4,5,6,7,8,9,10)

# how about a function with unlimited keyword parameters?
# the variable declaration with use two asterisks followed by the name of the parameter collection
# normally like **kwargs    (meaning keyword arguments)
# items come in as a dictionary and can be accessed by their key
# kwargs["add"], for example
# def calculate(n, **kwargs):
#     # for (key,value) in kwargs.items():
#     #     print(f"key - {key}, value - {value}")
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply=5)

#when working with dictionaries, using the brackets to access a key will throw an error if the 
#key is not present.
#dictionary.get("key") will return None if the key doesn't exist

# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")

# # all of these are fine
# firstCar = Car(make = "Nissan")
# secondCar = Car(make = "Infiniti", model = "J30")
# thirdCar = Car(make = "Honda", model = "Accord", color = "\"Beige\"")
# fourthCar = Car(make = "Nissan", model = "Altima", color = "White", seats = "4")
# fifthCar = Car(make = "Tesla", model = "Y", color = "Blue", seats = "4", engineType = "Electric")


converter = MilesToKmConverter()
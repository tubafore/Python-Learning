class BandNameGenerator:
    # THE constructor name
    # the first argument is to reference members, typically called self
    # there is no such thing as public/private/protected in python
    def __init__(self):
        city = "";
        pet = "";

    # a method that accesses internal fields
    def DoTheThing(self):
        print("Welcome to the Band Name Generator")
        self.city = input("What's the name of the city you grew up in?\n")
        self.pet = input("What's your pet's name?\n")
        return self.Generate()
    
    def Generate(self):
        return f"{self.city} {self.pet}"

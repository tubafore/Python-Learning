import random

class PasswordGenerator:
    def __init__(self) -> None:
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def Generate(self) -> str:
        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []

        password_list.extend([random.choice(self.letters) for _ in range(nr_letters)])
        password_list.extend([random.choice(self.symbols) for _ in range(nr_symbols)])
        password_list.extend([random.choice(self.numbers) for _ in range(nr_numbers)])
        # for char in range(nr_letters):
        #     password_list.append(random.choice(self.letters))

        # for char in range(nr_symbols):
        #     password_list += random.choice(self.symbols)

        # for char in range(nr_numbers):
        #     password_list += random.choice(self.numbers)

        random.shuffle(password_list)

        return "".join(password_list)

        
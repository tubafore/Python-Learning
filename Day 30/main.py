from passwordManager import *

program = PasswordManager()


# try/except/catch/finally notes

# try: #like all other try statements
#     file = open("a_file.txt")
# except FileNotFoundError as errorMessage: #this is the catch equivalent in python, you can name the error if you want to use it
#     file = open("a_file.txt", "w")
#     print(f"Opening the file failed with error: {errorMessage}")
#     file.write("Something")
# else: #what happens when there is no exception
#     content = file.read()
#     print(content)
# finally: #always gets run after the try + except/else blocks
#     file.close()
#     print("File was closed.")

# raise KeyError("This is an error I made up") # a throw statement equivalent


from tkinter import *
from tkinter import messagebox
from passwordGenerator import PasswordGenerator
import pyperclip

class PasswordManager:
    LOWERS = "abcdefghijklmnopqrstuvwxyz"
    UPPERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "01234567890"
    SYMBOLS = r",./;[]\`-=<>?:{}|~!@#$%^&*()_+"

    def __init__(self) -> None:
        self.window = Tk()
        #self.form = ttk.Frame(self.window, padding="20") # left top right bottom
        self.canvas = Canvas(width=200, height=200)
        self.image = PhotoImage(file="logo.png")
        self.imageId = -1
        self.labelWebsite = Label(text="Website:")
        self.labelUsername = Label(text=r"Email/Username:")
        self.labelPassword = Label(text="Password:")
        #  ********** ATTENTION **************
        #  THESE ARE CALLED ENTRY NOT TEXT!!!!
        #  ***********************************
        self.txtWebsite = Entry(width=35)
        self.txtUsername = Entry(width=35)
        self.txtPassword = Entry(width=21)
        self.btnGenerate = Button(text="Generate Password", command=self.generatePassword)
        self.btnAdd = Button(text="Add", width=36, command=self.addPassword)
        self.passwordGenerator = PasswordGenerator()
        self.setupUI()

        self.window.mainloop()

    #grid sticky notes:
    #  this "sticks" the control on the N - North, S - South, E - East, and/or W - West side
    #  so, if you want a control to stick to the edges of its grid spot, sticky="EW" will 
    #  stick it to the east and west sides
    def setupUI(self) -> None:
        #self.form.grid()
        self.window.title("Password Manager")
        self.window.configure(padx=50, pady=50)
        self.imageId = self.canvas.create_image(100, 100, image=self.image) # x position, y position of the center of the image
        self.canvas.grid       (row=0, column=1)
        self.labelWebsite.grid (row=1, column=0, sticky="W", pady=(0,10))  #adding a top padding of 0 and a bottom padding of 10 to space things out a little
        self.txtWebsite.grid   (row=1, column=1, columnspan=2, sticky="EW", pady=(0,10))
        self.txtWebsite.focus()
        self.labelUsername.grid(row=2, column=0, sticky="W", pady=(0,10))
        self.txtUsername.grid  (row=2, column=1, columnspan=2, sticky="EW", pady=(0,10))
        self.txtUsername.insert(index=END, string="tubafore@gmail.com")
        self.labelPassword.grid(row=3, column=0, sticky="W", pady=(0,10))
        self.txtPassword.grid  (row=3, column=1, sticky="EW", pady=(0,10), padx=(0, 3)) #adding a left padding of 0 and right padding of 3 to space things out a little
        self.btnGenerate.grid  (row=3, column=2, pady=(0,10))
        self.btnAdd.grid       (row=4, column=1, columnspan=2, sticky="EW", pady=(0,10))

    def generatePassword(self) -> None:
        self.txtPassword.delete(0, END)
        self.txtPassword.insert(END, self.passwordGenerator.Generate())
        pyperclip.copy(self.txtPassword.get())

    def addPassword(self) -> None:
        website = self.txtWebsite.get()
        username = self.txtUsername.get()
        password = self.txtPassword.get()

        if self.validateForm(website, username, password):
            if messagebox.askokcancel(title=f"Confirm details for {website}", message=f"You entered\nUsername: {username}\nPassword: {password}"):
                with open("data.txt", mode="a") as file:
                    file.write(f"{website}\t{username}\t{password}\n")
                self.clearForm()
        else:
            messagebox.showerror(title="Incomplete form", message="Please fill in each field.")

    def validateForm(self, website:str, username:str, password:str) -> bool:
        result = True
        website = website.strip()
        username = username.strip()
        password = password.strip()
        result &= (website != "" and website != None)
        result &= (username != "" and username != None)
        result &= (password != "" and password != None)
        return result
        

    def clearForm(self) -> None:
        self.txtPassword.delete(0, END)
        self.txtWebsite.delete(0, END)
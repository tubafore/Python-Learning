#tkinter is the GUI library for python

import tkinter
import random

#create a window
window = tkinter.Tk()
#setup the window
window.title("My first GUI Program")
window.minsize(width=800, height=600)

#let's add stuff to the window
label = tkinter.Label(text="I am a label", font=("Arial", 24)) #must be added to the window
#this adds it to the window with the default settings.  It can get much more specific though
#set properties on it by either using it like a dictionary
label["text"] = "New Text"
#or by calling the configure method with the parameter you want to change
label.configure(background = "magenta") #because we have to

#a text box
entry = tkinter.Entry(width=40)
entry.insert(tkinter.END, string="Some placeholder text")

def buttonClicked():
    label.config(text= entry.get()) #gets the text from the entry
button = tkinter.Button(text="Click Me!", command=buttonClicked)
# button.configure(command=buttonClicked)

#a multi-line text box
text = tkinter.Text(height=5, width=30) #these heights and widths are in lines/characters
#more placeholder text
text.insert(tkinter.END, "Example of multi-line text entry placeholder text")
#Gets current value in the textbox at line 1, character 0 (the 1.0 part) to the end of the entry
print(text.get("1.0", tkinter.END))
#and let's focus the cursor in there
text.focus()


#the event fired when the user interacts with the spinbox
def spinbox_used():
    #get the current value of the spinbox
    print(spinbox.get())

#a numeric updown
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)

#the event fired when the user interacts with the scale
#note that this one has an argument
def scale_used(value):
    print(value)

#Scale, aka a slider
scale = tkinter.Scale(from_=0, to=100, command=scale_used)

#the event fired when the user interacts with the checkbox
def checkbutton_used():
    #Prints 1 if "Is On?" button checked, otherwise 0
    print(checked_state.get())

#variable to hold on to checked state, 0 is off, 1 is on
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)

#radio buttons!

#on change eventhandler
def radio_used():
    print(radio_state.get())

#Variable to hold on to which radio button value is checked
#this also uses IntVar
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)

#listbox
#note we have an argument in the handler
def listbox_used(event):
    #Gets the current selection from the listbox
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4) #height is given in lines
#make a list of things to go in there
fruits = ["Apple", "Pear", "Orange", "Banana"]
#insert each item at the provided index
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used) #see the documentation for the meaning of this magic string and how to make a different one


#label.pack()
#button.pack()
#entry.pack()
# text.pack()
# spinbox.pack()
# scale.pack()
# checkbutton.pack()
# radiobutton1.pack()
# radiobutton2.pack()
# listbox.pack()

#we can also position things using place, providing an (x,y) coordinate (starting from the top left)
#label.place(x=0,y=0) #in the top left

#we can also use the grid layout manager, but can't use pack with grid
def somethingDifferent():
    anotherButton.configure(bg=random.choice(["red", "blue", "green", "magenta"]))

anotherButton = tkinter.Button(text="Do something different", command=somethingDifferent)

label.grid(row=0, column=0)
anotherButton.grid(row=0, column=2)
button.grid(row=1, column=1)
entry.grid(row=2, column=3)

#let's style this
window.configure(padx=20, pady=20)
label.configure(padx=50, pady=50)

#will make the program stay open
window.mainloop()
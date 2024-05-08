import random
import pandas
from NatoPhoneticTranslator import NatoPhoneticTranslator

#list comprehension notes
#this is a new topic to you
#list comprehension = creating a list from an existing list
#syntax:  newList = [newItem for item in existingList]
#to help remember the syntax, write out that every time then just fill it in

existingList = [1, 2, 3]
newList = []
for n in existingList:
    add1 = n + 1
    newList.append(add1)

#all that becomes
newListFromComprehension = [n+1 for n in existingList]
print(existingList)
print(newList)
print(newListFromComprehension)

#it works on other sequences (strings, lists, ) too, like strings
name = "Jonathan"
namePlus1 = [chr(ord(letter) + 1) for letter in name]
print(name)
print(namePlus1)

#double numbers in range(1,5)
print([n*2 for n in range(1,5)])

#list comprehension with condition!
#syntax: newList = [newItem for item in existingList if condition]
#type this one out too to remember it
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freedie"]
shortNames = [name for name in names if len(name) < 5]
print(shortNames)

#take the long names and make them uppercase
print([name.upper() for name in names if len(name) >= 5])

#square the numbers in the list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]

#get just the even numbers from an string of comma separated numbers, only run this in the auditorium thing
# result = [int(n) for n in numbers if int(n) % 2 == 0]

# with open("file1.txt") as file1:
#     file1Contents = file1.readlines()
# with open("file2.txt") as file2:
#     file2Contents = file2.readlines()

# numberSet1 = [int(n.strip()) for n in file1Contents]
# numberSet2 = [int(n.strip()) for n in file2Contents]

# result = [number for number in numberSet1 if number in numberSet2]

# from statesGame import StatesGame

# game = StatesGame()
# game.Play()

#dictionary comprehension notes
#syntax:  newDictionary = {newKey:newValue for item in list}
#__or__
#newDictionary = {newKey:newValue for (key,value) in dictionary.items()}
#write that in for practice with the syntax

#generate a new dictionary with random scores for the names in the names list
studentScores = {student:random.randint(0,100) for student in names}
print(studentScores)

#generate a new dictionary with the students above that passed
passedStudents = {student:score for (student,score) in studentScores.items() if score >= 60 }
print(passedStudents)

# generate a new dictionary with the individual words of a sentence paired with its length.  Include punctation
# sentence = "What is the airspeed velocity of an unladen swallow?"
# words = sentence.split(" ")
# result = {word:len(word) for word in words}
# print(result)

# generate a new dictionary with a day,temperature pair in celcius is converted to F
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:((tempC * 9 /5) + 32) for (day, tempC) in weather_c.items()}

#how to iterate through a dictionary accessing both the key and value
for (key, value) in studentScores.items():
    print(value)

#looping through a pandas DataFrame, make sure your data is structured properly, studentScores up there won't work
studentDictionary = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}
studentDataFrame = pandas.DataFrame(studentDictionary)
#getting each column's value/key
for (key, value) in studentDataFrame.items():
    print(key)

#loop through the rows of the dataframe
for (index, row) in studentDataFrame.iterrows():
    print(f"{row["student"]} got {row.score}") 

translator = NatoPhoneticTranslator()
translator.Translate()



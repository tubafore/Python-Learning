#working with CSV

#the hard way
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     for i in range(len(data)):
#         data[i] = data[i].strip()
#
# print(data)

#import csv

#read the file using the csv reader and get the data from the temps column, putting into an int list
# with open("weather_data.csv") as file:
#     temperatures = []
#     reader = csv.reader(file)
#     row1 = True
#     for row in reader:
#         if row1:
#             row1 = False
#             continue
#         temperatures.append(int(row[1]))
# print(temperatures)

# read the file with csv DictReader, get the data from the temps column, putting into an int list
# with open("weather_data.csv") as file:
#     reader = csv.DictReader(file)
#     temps = []
#     for row in reader:
#         temps.append(int(row['temp']))
# print(temps)

# Get all the info from the file using pandas, get the data from the temps column, putting into an int list
# import pandas  
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"].to_list())
# # a DataFrame object
# # a 2-D representation of the data
# # ex. a whole sheet from Excel
# # print(type(data))
# # a Series object
# # a single column of data
# # print(type(data["temp"]))

# #how about getting the average of that data?
# print(f"average temperature was {data["temp"].mean()}")
# #how about getting the max of that data?
# print(f"max temp is {data["temp"].max()}")
# #time for magic, it takes each column header and puts an attribute on the DataFrame for you
# #the following two lines are equivalent
# #match the cases
# print(data["condition"])
# print(data.condition)
# #get the row for Monday
# print(data[data.day == "Monday"])
# #get the row for the day where the temperate was at its maximum
# print(data[data["temp"] == data["temp"].max()])
# #get the condition of monday
# monday = data[data.day == "Monday"]
# print(monday.condition)
# #monday's temperature in F
# print(f"Monday's temp in F: {(monday.temp * 9/5) + 32}")

# #creating a pandas dataframe
# dataDictionary = {
#     "students": ["Amy", "James", "Angela"],
#     "scores" : [76, 67, 65]
# }
# handcrafted = pandas.DataFrame(dataDictionary)
# #convert it to a csv file
# handcrafted.to_csv("new data.csv")


# Import the data from that long csv file, take counts of the individual
# colors and save them to a different csv file
# import pandas

# squirrelPath = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
# squirrelData = pandas.read_csv(squirrelPath)
# furColors = squirrelData["Primary Fur Color"].value_counts()
# results = {
#     "Fur Color" : [],
#     "Count" : []
# }

# for i in furColors.index:
#     results["Fur Color"].append(i)
# for v in furColors.values:
#     results["Count"].append(v)

# pandas.DataFrame(results).to_csv("squirrel_count.csv")

from statesGame import StatesGame

game = StatesGame()
game.Play()
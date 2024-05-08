from assignment import SilentAuction

#dictionary day
#setting items in the initialization {Key: value}
def dictionaryInfo():
    programmingDictionary = { 
        "Bug": "An error in a program that prevents the program from running as expected.",
        "Function": "A piece of code that you can easily call over and over again."
    }
    #retrieve an item with dictionary[Key]
    print(programmingDictionary['Bug'])
    
    #add a new value with dictionary[New Key] = value
    programmingDictionary["Loop"] = "The action of doing something over and over again."
    print(programmingDictionary["Loop"])

    #create an empty dictionary
    emptyDictionary = {}

    #clear a dictionary
    #programmingDictionary = {}

    #redefine an item
    print(programmingDictionary["Bug"])
    programmingDictionary["Bug"] = "A moth in your computer."
    print(programmingDictionary["Bug"])

    #looping through a dictionary loops through just the keys
    for key in programmingDictionary:
        print(key)
        print(programmingDictionary[key])

def gradeInterpreter():
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99, 
        "Draco": 74,
        "Neville": 62,
    }

    student_grades = {}
    for key in student_scores:
        if student_scores[key] <= 70:
            student_grades[key] = "Fail"
        elif student_scores[key] <= 80:
            student_grades[key] = "Acceptable"
        elif student_scores[key] <= 90:
            student_grades[key] = "Exceeds Expectations"
        else:
            student_grades[key] = "Outstanding"
         
    print(student_grades)

#nesting notes
#you can have values as lists or other dictionaries
#basic
def nestingNotes():
    capitols = {
        "France":"Paris",
        "Germany": "Berlin"
    }

    #nesting a list in a dictionary
    travelLog = {
        "France":["Paris", "Lille", "Dijon"],
        "Germany":["Berlin", "Hamburg", "Stuttgart"]
    }

    alsoValid = ['1', '2', ['3','4']] #but don't, it's annoying

    #nesting a dictionary in a dictionary
    expandedTravelLog = {
        "France":{"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
        "Germany":{"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 15}
    }

    #nesting a dictionary in a list
    gettingComplexTravelLog = [
        { 
            "country" : "France",
            "cities_visited": ["Paris", "Lille", "Dijon"], 
            "total_visits": 12
        },
        {
            "country" : "Germany",
            "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
            "total_visits": 15
        }
    ]

    for entry in gettingComplexTravelLog:
        print(entry["country"])

nestingNotes()

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country:str, visits:int, list_of_cities:list):
    travel_log.append({
        "country" : country,
        "visits" : visits,
        "cities" : list_of_cities
    })

auction = SilentAuction()
auction.startAuction()
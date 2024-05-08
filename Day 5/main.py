from assignment import PasswordGenerator

#general note
#a colon establishes a scope in python

#for loops
#much more like a foreach loop in c#
def forLoops():
    fruits = ["apples", "peaches", "pears"]
    for fruit in fruits:
        print(fruit)

#can't use len 
def averageHeights(student_heights:list):
    total = 0
    count = 0
    for height in student_heights:
        total += height
        #no ++ in python
        count += 1
    print(f"total height = {total}")
    print(f"number of students = {count}")
    print(f"average height = {round(total/count)}")

#can't use max
def highScore(student_scores:list):
    max = -99999999999
    for score in student_scores:
        if score > max:
            max = score
    print(f"The highest score in the class is: {max}")

#range notes
#produces values between the start value (inclusive) to the end value (exclusive)
#an optional 3rd parameter specifies the interval
def rangeLooping():
    fruits = ["apples", "peaches", "pears"]
    #essentially for (i = 0; i < fruits.Length; i++)...
    for i in range(0, len(fruits)):
        print(fruits[i])


def sumAllEvenNumbers(target:int):
    if target > 0 and target < 1000:
        target += 1
        total = 0
        for i in range(0, target, 2):
            total += i
        print(total)

def fizzBuzz(first:int, second:int):
    if first < second:
        third = first * second
        for i in range(1, 101):
            if i % third == 0:
                print("FizzBuzz")
            elif i % second == 0:
                print("Buzz")
            elif i % first == 0:
                print("Fizz")
            else:
                print(f"{i}")

PasswordGenerator.Generate()
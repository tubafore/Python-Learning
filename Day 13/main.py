# this are a series of debugging issues to solve

############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   #for i in range(1, 20): #wasn't getting to 20
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# try to figure out how to reproduce the bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# #dice_num = randint(1, 6) #this will fail when randint returns 6
# dice_num = randint(0, 5) 
# print(dice_imgs[dice_num])

# Play Computer
# trace through the code like a programmer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# #elif year > 1994: #if the {year} = 1994, nothing happens
# elif year >= 1994: 
#   print("You are a Gen Z.")

# # Fix the Errors
# duh
# #age = input("How old are you?") #should be converted to an int
# age = int(input("How old are you?"))
# if age > 18:
# #print("You can drive at age {age}.") #should be an f string and indented
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# like we're debugging javascript back in the aughts
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# #word_per_page == int(input("Number of words per page: ")) #using double equals for an assignment doesn't really work
# word_per_page = int(input("Number of words per page: "))
# print(f'pages = {pages}')
# print(f"words_per_page = {word_per_page}") #would you look at that it's still 0
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# now we're on the real programmer tool
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  #b_list.append(new_item) #we can see it's not indented properly, so it's only happening once
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
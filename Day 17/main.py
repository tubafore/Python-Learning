#making our "first" class!
#names of classes are PascalCase
#for some reason you'll use snake_case for everything else
"""class User:
    def __init__(self, userId, userName) -> None:
        self.id = userId
        self.userName = userName
        #setting a default value without a parameter
        self.followers = 0
        self.following = 0
    
    def doesNothing():
        #to make anything with no implementation details, use "pass"
        pass

    def follow(self, user):
        user.followers += 1
        self.following += 1
        

user1 = User("001", "angela")
#putting attributes (fields) on just this instance
#another User instance wouldn't have this attribute
user1.emailAddress = "angela@pythondev.com"

print(user1.userName)

user2 = User("002", "jack")
user1.follow(user2)

print(user2.followers)"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []
for question in question_data:
    questionBank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(questionBank)
quiz.Run()

from question_model import Question

#type alias for autocomplete goodness maybe?
type QuestionList = list[Question]

class QuizBrain:
    def __init__(self, questionList:QuestionList) -> None:
        self.questionNumber = 0
        self.questions = questionList
        self.answerChoices = ["t", "true", "f", "false"]
        self.score = 0

    def Run(self) -> None:
        while self.questionNumber < len(self.questions):
            self.nextQuestion()
        print("You've completed the quiz")
        print(f"Your final score is: {self.score}/{self.questionNumber}")
        
    
    def convertAnswer(self, userAnswer:str) -> str:
        if userAnswer == "t":
            userAnswer = "true"
        elif userAnswer == "f":
            userAnswer = "false"
        userAnswer = userAnswer.title()
        return userAnswer

    def checkAnswer(self, question:Question, userAnswer:str) -> None:
        if question.answer == userAnswer:
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, you got it wrong")

    def nextQuestion(self) -> None:
        if self.questionNumber < len(self.questions):
            question = self.questions[self.questionNumber]
            userAnswer = input(f"Q.{self.questionNumber + 1}: {question.text} (True/False)? ").lower()
            while userAnswer not in self.answerChoices:
                print("invalid answer, try again")
                userAnswer = input(f"Q.{self.questionNumber + 1}: {question.text}").lower()

            userAnswer = self.convertAnswer(userAnswer)
            self.checkAnswer(question, userAnswer)
            
            print(f"The correct answer was: {question.answer}.")
            print(f"Your current score is: {self.score}/{self.questionNumber + 1}")
            print("\n")

            self.questionNumber += 1

                
            




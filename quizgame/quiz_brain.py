class Quiz:
    def __init__(self, list):
        self.number = 0
        self.list = list
        self.score = 0
    def still(self):
        return self.number<len(self.list)
    def next(self):
        text = self.list[self.number].text
        self.number += 1
        user_answer = input(f"Q{self.number}. {text} (True/False) ")
        self.check(user_answer, self.list[self.number-1].answer)
    def check(self, user_answer, correct):
        if user_answer.lower() == correct.lower() :
            print('You got it right!')
            self.score += 1
            print(f"{self.score}/{self.number}")
            print()
        else:
            print('You got it wrong!')
            print(f"{self.score}/{self.number}")
            print()



class QuizBrain:
    
    def __init__(self, q_list) -> None:
        self.q_number = 0
        self.quizzlist = q_list
        self.point = 0
        
    def still_have_question(self):
        if self.q_number < len(self.quizzlist):
            return True
        else :
            return False
            
    def check_answer(self, user_answer, current_question):
        if user_answer == current_question.answer :
            self.point += 1
            return print("맞았습니다.")
            
        else:
            return print("틀렸습니다.")
        

    def next_question(self):
        current_question = self.quizzlist[self.q_number] #q_number에 해당되는 질문과 답 리스트를 cureent_question에 저장
        self.q_number += 1
        user_answer = input(f"Q. {self.q_number}. {current_question.text}? (예/아니오) : ")
        return self.check_answer(user_answer, current_question)
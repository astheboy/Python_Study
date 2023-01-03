from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for quiz in question_data :
    s_quiz = Question(quiz["text"], quiz["answer"])
    question_bank.append(s_quiz)

s_brain = QuizBrain(question_bank)

while s_brain.still_have_question():
    s_brain.next_question()


print(f"당신의 최종 점수 : {s_brain.point}")
# print("question_bank 리스트에 date의 질문과 답이 메모리에 저장")    
# print(question_bank)
# print(len(question_bank))
# print("question_bank의 0번 인덱스에 들어가 있는 질문과 답을 출력")

# for i in range(0, len(question_bank)):
#     print(f"{i}번 문제 : {question_bank[i].text}")
#     print(question_bank[i].answer)
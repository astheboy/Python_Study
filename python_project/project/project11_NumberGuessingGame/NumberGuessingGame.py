# 함수
# random_number_function : 랜덤으로 1~100까지의 숫자를 추출하는 함수
# guessing_number_funcion : 사용자가 추측한 수와 랜덤 수를 비교하고 결과물을 출력하는 함수
# game_function : 게임 진행 함수

# 변수
# difficult_level : 난이도 변수(easy, hard)

# 딕셔너리
# number_of_attempts : 시도 횟수(easy : 10, hard : 5)

import random
from art import logo

# 랜덤 수 생성 함수
def random_number_function(max_number):
    random_number = random.randint(1, max_number)
    return random_number

# print(random_number_function(max_number))

# 랜덤 숫자와 추측 숫자 비교하는 함수
def guessing_number_function(random_number, user_guess_number, difficlut_level):
    print(f"시도 횟수 : {difficlut_level}")
    if random_number > user_guess_number :
        print("낮았어요. 더 높은 수를 추측해 보세요. : ")
        # user_guess_number = int(input("더 높은 수를 추측해 보세요. : "))
        # return user_guess_number
        game_on = True
        return game_on
    elif random_number < user_guess_number :
        print("높았어요. 더 낮은 수를 추측해 보세요. : ")
        # user_guess_number = int(input("더 낮은 수를 추측해 보세요. : "))
        # return user_guess_number
        game_on = True
        return game_on
    elif random_number == user_guess_number :
        print(f"맞았어요 정답은 {random_number}입니다.")
        if input("게임을 다시 시작하겠습니까? (yes, no) : ") == "yes" :
            game_function()
        else:
            game_on = False
            return game_on
            

def game_function():
    
    #logo 출력
    print(logo)

    max_number = int(input("숫자 추측하기 퀴즈에 사용할 가장 큰 숫자를 입력해 주세요 : "))

    # 딕셔너리 정의
    number_of_attempts = {'easy': 10, "hard" : 5}
    difficult_level = number_of_attempts[input("퀴즈 난이도를 선택하세요.(easy, hard) :  ")] 
            
    # 랜덤 수 생성 함수호출
    random_num = random_number_function(max_number)

    while difficult_level != 0 :
        user_guess_number = int(input(f"당신이 생각한 수를 입력해주세요. (1 ~ {max_number}) : "))
        game_on = guessing_number_function(random_num, user_guess_number, difficult_level)
        
        difficult_level -= 1
        if difficult_level == 0 :
            print("횟수를 초과하였습니다.")
            game_function()
        if not game_on :
            print("게임을 종료하겠습니다.")
            return

game_function()



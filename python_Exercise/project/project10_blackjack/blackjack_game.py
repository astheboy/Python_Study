
import random

# 게임 진행 변수
game_in_progress = True
# 게임 카드를 저장하는 딕셔너리
game_card = {"user":[], "diler":[]}
# 카드를 뽑는 횟수
game_index = 1
# 전체 카드를 저장할 리스트
card_list = []

#트럼프 카드의 모양과 숫자를 결합하여 트럼프 카드 리스트를 생성 및 랜덤 카드를 추출하는 함수
def get_card_function(game_index, card_list):
    if game_index == 1:
        
        card_symbol = ["Spade","Clover","Heart","Diamond"]
        card_dic = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":[1, 11]}
        for symbol in card_symbol :
            for number in list(card_dic.keys()):
                card = symbol+" "+number
                card_list.append(card)
    # 전체 리스트에서 랜덤 카드를 추출
    get_card = random.choice(card_list)
    # 전체 리스트에서 추출한 랜덤 카드를 빼서 다음 리스트에서 중복되어 카드가 뽑히지 않도록 하기
    card_list = list(set(card_list)-set(get_card))
    return get_card, card_list

# 카드의 숫자 중 알파벳 카드를 체크 후 알파벳을 숫자로 변경한 후 해당 숫자값 합을 구하는 함수
def symbol_card_check(card_number_list):
    
    card_sum_result = 0
    # A카드의 경우 점수를 1과 11로 두 가지 선택조건이 있기 때문에 미리 추출된 카드 숫자 리스트(card_number_list)를 복사해 놓기 위한 리스트 선언
    a_card_list = []
    # 카드 숫자 리스트(card_number_list)에서 알파벳이 포함된 인덱스를 모두 추출하여 저장할 리스트 선언
    alpabet_index_list= []

    # 카드 알파벳이 A인 경우 처리
    if "A" in card_number_list :
        a_card_list = card_number_list

         #"A"문자가 포함된 리스트의 인덱스를 모두 추출하는 코드
        alpabet_index_list = [i for i in range(len(card_number_list)) if card_number_list[i]=="A"]
        # "A"문자를 1의 값으로 계산하여 합을 구하는 코드
        for i in range(len(alpabet_index_list)):
            card_number_list[alpabet_index_list[i]] = 1
        for b in range(len(card_number_list)):
            card_number_list[b] = int(card_number_list[b])
        a_card_sum_1 = sum(card_number_list)

        # "A"문자를 11의 값으로 계산하여 합을 구하는 코드
        alpabet_index_list = [i for i in range(len(a_card_list)) if a_card_list[i]=="A"]
        for i in range(len(alpabet_index_list)):
            card_number_list[alpabet_index_list[i]] = 11
        for b in range(len(a_card_list)):
            a_card_list[b] = int(a_card_list[b])
        a_card_sum_11 = sum(a_card_list)

        # "A" 문자를 1과 11로 계산한 결과 값을 비교하여 큰 값을 선택한 후 전체 리스트의 합에 더하는 코드
        if a_card_sum_1 < 21 and a_card_sum_11 < 21 :
            if a_card_sum_11 > a_card_sum_1 :
                card_sum_result = a_card_sum_11
            else:
                card_sum_result = a_card_sum_1
    
    else:
        # "J, Q, K" 카드를 숫자로 변환하는 코드
        if "J" in card_number_list :
            alpabet_index_list = [i for i in range(len(card_number_list)) if card_number_list[i]=="J"]
            for i in range(len(alpabet_index_list)):
                card_number_list[alpabet_index_list[i]] = 10
        elif "Q" in card_number_list :
            alpabet_index_list = [i for i in range(len(card_number_list)) if card_number_list[i]=="Q"]
            for i in range(len(alpabet_index_list)):
                card_number_list[alpabet_index_list[i]] = 10
        elif "K" in card_number_list :
            alpabet_index_list = [i for i in range(len(card_number_list)) if card_number_list[i]=="K"]
            for i in range(len(alpabet_index_list)):
                card_number_list[alpabet_index_list[i]] = 10
        
        # (알파벳이 없거나 알파벳이 "J, Q, K"를 숫자로 변경한 경우) 리스트의 숫자를 모두 합하여 card_sum_result로 저장
        for b in range(len(card_number_list)):
            card_number_list[b] = int(card_number_list[b])
        card_sum_result = sum(card_number_list)
    
    return card_sum_result

# 합산된 결과 값을 이용하여 승리자를 결정하는 함수
def winner_check(user_point, user_bet_point):
    diler_card_sum = 0
    user_card_sum = 0
    diler_card_number = []
    user_card_number =[]

    # game_card 딕셔너리에서 'diler' 키 값의 리스트에 저장된 카드를 1개씩 불러와 공백을 기준으로 잘라내어 순수하게 숫자만 추출하기
    for diler_card in game_card["diler"]:
        diler_card_number.append(diler_card.split()[1])
    # 숫자만 추출된 리스트를 symbol_card_check 함수로 보내 알파벳을 처리하여 리스트 숫자를 합산하고 결과값을 diler_card_sum 변수에 저장
    diler_card_sum = symbol_card_check(diler_card_number)    
    
    # game_card 딕셔너리에서 'user' 키 값의 리스트에 저장된 카드를 숫자만 추출하여 딜러 카드과 동일한 과정으로 처리
    for user_card in game_card['user']:
        user_card_number.append(user_card.split()[1])
    user_card_sum = symbol_card_check(user_card_number)
    
    # 딜러 카드가 16점 이하인 경우 딜러에게 카드를 1장 더 뽑고 점수를 합하기
    if diler_card_sum <= 16:
            extra_card_num = []
            print("\n딜러 카드 합이 16 이하이므로 1장의 카드를 더 받습니다.")

            game_card['diler'].append(get_card_function(game_index, get_card_function(game_index,card_list)[1])[0])
            diler_extra_card = game_card['diler'][2:]

            for extra_card in diler_extra_card:
                extra_card_num.append(extra_card.split()[1])
            diler_extra_card_sum = symbol_card_check(extra_card_num)
            diler_card_sum += diler_extra_card_sum
            
            print("딜러 카드: ", end='')
            for i in range(len(game_card['diler'])):
                print(f"{game_card['diler'][i]}, ", end="")

    # 딜러와 유저의 합한 값이 21보다 작은 경우 서로의 값을 비교하여 승부를 결정짓는 코드
    if diler_card_sum < 21 and user_card_sum < 21:
        if diler_card_sum > user_card_sum:
            print("\n딜러가 이겼습니다.")
            user_point -= user_bet_point
            print(f"당신은 {user_bet_point}포인트를 잃어 현재 {user_point}포인트가 되었습니다.")
        else: 
            print("\n당신이 이겼습니다.")
            user_point += user_bet_point * 2
            print(f"당신은 {user_bet_point*2}포인트를 얻어 현재 {user_point}포인트가 되었습니다.")
    else :
    
    # 2장의 카드를 받으상태에서 블랙잭을 처리하는 코드
        if len(game_card["diler"]) == 2:
            if diler_card_sum == 21:
                print(f"딜러가 {diler_card_sum}으로 블랙잭입니다. 당신이 졌습니다.")
                user_point -= user_bet_point
                print(f"당신은 {user_bet_point}포인트를 잃어 현재 {user_point}포인트가 되었습니다.")
        if len(game_card["user"]) == 2:
            if user_card_sum == 21 :
                print(f"당신은 {user_card_sum}을 얻어 블래잭입니다. 1.5배 상금을 받습니다.")
                user_point += user_bet_point * 2 + user_bet_point * 1.5
                print(f"당신은 {user_bet_point * 2 + user_bet_point * 1.5}포인트를 얻어 현재 {user_point}포인트가 되었습니다.")
        if user_card_sum > 21:
            print(f"당신의 점수는 {user_card_sum}이므로 21점을 초과하였습니다.")
            print("당신은 졌습니다.")
        
    return 

        
#게임 시작과 함께 딜러는 두장의 카드를 받고 1장의 카드만 화면으로 보여주는 코드
for k in range(2) :
    game_card['diler'].append(get_card_function(game_index, get_card_function(game_index,card_list)[1])[0])

# 게임 시작 전 포인트를 배팅하는 코드
print(f"딜러 카드 : {game_card['diler'][0]}, * \n")
user_point = 10000
print(f"당신은 현재 {user_point}포인트가 있습니다.")
user_bet_point = int(input("당신은 몇 포인트를 내겠습니까?"))

# 게임 과정 코드
while game_in_progress :

    get_card_turn = input("\n카드를 받으시겠습니까? (y, n)")
    
    if get_card_turn == "n" :
        game_in_progress = False
        print(f"\n딜러 카드 : {game_card['diler'][0]}, {game_card['diler'][1]}")
        print("당신 카드: ", end='')
        for i in range(game_index-1):
            print(f"{game_card['user'][i]}, ", end="")
        winner_check(user_point, user_bet_point)
        
    else:
        game_card['user'].append(get_card_function(game_index, get_card_function(game_index,card_list)[1])[0])
        print("\n당신 카드: ", end='')
        for i in range(game_index):
            print(f"{game_card['user'][i]}, ", end="")
        game_index += 1

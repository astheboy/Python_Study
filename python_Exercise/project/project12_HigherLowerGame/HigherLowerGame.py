import random

from art import logo, vs
from game_data import data

# 프로그램 1차 버전

# result_list = ["", ""]
# people_list =[]
# def follower_cacl(first_people, second_people):
#     # 팔로우 계산한 후 result 리스트에 결과값 넣기
#     first_people_follower = first_people["follower_count"]
#     second_people_follower = second_people["follower_count"]

#     if first_people_follower > second_people_follower :
#         result_list[0] = first_people
#         result_list[1] = "A"
#     else:
#         result_list[0] = second_people
#         result_list[1] = "B"
    
#     return result_list

# def people_select(result_list, data, people_list):
#     answer_count = 0
    
#     while data != [] :
#         # 랜덤하기 두 인물을 뽑기
#         if result_list[0] == "":
#             people_list.append(data[random.randint(0, len(data))])
#             first_people = people_list[0]
#             data = [x for x in data if x not in people_list]
#             second_people = data[random.randint(0, len(data))]
#             people_list.append(second_people)
#             result_list = follower_cacl(first_people, second_people)
            
#         else:
#             first_people = result_list[0]
#             data = [x for x in data if x not in people_list]
#             second_people = data[random.randint(0, len(data))]
#             people_list.append(second_people)
#             result_list = follower_cacl(first_people, second_people)
        
#         print(f"첫번째 대상 A : {first_people['name']}, a {first_people['description']}, from {first_people['country']}")
#         print(vs)
#         print(f"두번째 대상 B : {second_people['name']}, a {second_people['description']}, from {second_people['country']}")
        
#         answer = input("어떤 대상의 팔로우가 더 많을까요? (A or B) : ").upper()
#         answer_count += 1

#         if answer == result_list[1] :
#             print('맞았습니다.')
#             print(f"선택한 대상 {answer}의 팔로우 수 : {result_list[0]['follower_count']}백만")
#             print(len(data))
#         else:
#             print(f'틀렸습니다. 당신의 점수 : {answer_count}점')
#             print(len(data))
#             return  

# print(logo)
# people_select(result_list, data, people_list)


# # 프로그램 2차 버전

# result_list = ["","",""]

# def follower_cacl(first, second):
#     # 팔로우 계산한 후 result 리스트에 결과값 넣기

#     if first["follower_count"] > second["follower_count"] :
#         result_list = [first, second, "A"]
#     else:
#         result_list = [second, first, "B"]
    
#     return result_list

# def people_select(result_list, data):
#     answer_count = 0
    
#     while data != [] :
#         # 랜덤하기 두 인물을 뽑기
#         if result_list[0] == "":

#             first = data[random.randint(0, len(data))]
#             result_list[0] = first
#             data.remove(first)
#             second = data[random.randint(0, len(data))]
#             result_list[1] = second
#             data.remove(second)
    
#             result_list = follower_cacl(first, second)
            
#         else:
#             first = result_list[0]
#             second = data[random.randint(0, len(data))]
#             result_list[1] = second
#             data.remove(second)

#             result_list = follower_cacl(first, second)

#         print("\n")
#         print(f"첫번째 대상 A : {first['name']}, a {first['description']}, from {first['country']}")
#         print(vs)
#         print(f"두번째 대상 B : {second['name']}, a {second['description']}, from {second['country']}")
        
#         answer = input("어떤 대상의 팔로우가 더 많을까요? (A or B) : ").upper()
#         answer_count += 1

#         if answer == result_list[2] :
#             print(f'맞았습니다. 당신의 현재 점수 : {answer_count}')
#             # print(f"선택한 대상 {answer}의 팔로우 수 : {result_list[0]['follower_count']}백만")
#         else:
#             print(f'틀렸습니다. 당신의 점수 : {answer_count}점')
#             print(f"{result_list[0]['name']}의 팔로우 수 : {result_list[0]['follower_count']}백만")
#             print(f"{result_list[1]['name']}의 팔로우 수 : {result_list[1]['follower_count']}백만")
#             return  

# print(logo)
# people_select(result_list, data)


# 프로그램 3차 버전(유데미 강좌 코드 일부 추가)

result_list = ["","",""]

def format_print(account):
    """data 리스트에서 추출한 딕셔너리 요소를 각각의 포멧에 맞게 출력하는 함수

    Args:
        account (dictionary): data 리스트에서 랜덤하게 추출된 딕셔너리 요소

    Returns:
        _str_: 딕셔너리 키 값을 일정하게 배열한 문자열을 출력함
    """
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def follower_cacl(first, second):
    # 팔로우 계산한 후 result 리스트에 결과값 넣기

    if first["follower_count"] > second["follower_count"] :
        result_list = [first, second, "A"]
    else:
        result_list = [second, first, "B"]
    
    return result_list

def people_select(result_list, data):
    answer_count = 0
    second = random.choice(data)

    while answer_count != len(data) :
        # 랜덤하기 두 인물을 뽑기
        first = second
        second = random.choice(data)
        while first == second :
            second = random.choice(data)

        result_list = follower_cacl(first, second)
            

        print("\n")
        print(f"첫번째 대상 A : {format_print(first)}")
        print(vs)
        print(f"두번째 대상 B : {format_print(second)}")
        
        answer = input("어떤 대상의 팔로우가 더 많을까요? (A or B) : ").upper()
        answer_count += 1

        if answer == result_list[2] :
            print(f'맞았습니다. 당신의 현재 점수 : {answer_count}')
            # print(f"선택한 대상 {answer}의 팔로우 수 : {result_list[0]['follower_count']}백만")
        else:
            print(f'틀렸습니다. 당신의 점수 : {answer_count}점')
            print(f"{result_list[0]['name']}의 팔로우 수 : {result_list[0]['follower_count']}백만")
            print(f"{result_list[1]['name']}의 팔로우 수 : {result_list[1]['follower_count']}백만")
            return  

print(logo)
people_select(result_list, data)



import random
from hangman_art import stages, logo
from hangman_word import wordlist

blankword = []
end_of_game = False
userlife = len(stages)-1
startcount = len(stages)
finalcount = len(stages)

# 게임 시작 및 랜덤 단어 선택하기
print(logo)
print("** 단어 추측 행맨 게임 **")
print("단어를 추측해서 맞춰보세요.")
print("행맨을 꼭 살려주세요")


randomword = list(random.choice(wordlist)) # 문자열을 한 글자씩 끊어서 리스트로 바꾸기
len_randomword = len(randomword)

# 비어있는 단어 출력
for i in range(len_randomword) :
    blankword.append("_") 
print(blankword)
print()

# 단어 추측하기
print(f"당신이 단어를 맞출 수 있는 기회는 총 {startcount}회 입니다.")
print("비어있는 칸을 보고 예상되는 글자를 맞춰주세요.")
print()

while end_of_game == False :
    guessword = input("예상되는 글자를 입력해 주세요. : ")
    
    if guessword in blankword :
      print(guessword + "는 방금 전에 입력했습니다. ")
    else :
      if guessword in randomword :
        for i in range(len_randomword) :
          if randomword[i]== guessword :
            blankword[i] = guessword
      # randomwordindex = list(filter(lambda x : randomword[x] == guessword, range(len(randomword)))) #list에서 value 값으로 다중 index찾기
      # for i in range(len(randomwordindex)) :
      #     blankword[randomwordindex[i]] = guessword  #정답을 맞춘 글자로 바꾸기
        finalcount -= 1
        print(f"맞췄어요.")
        print(blankword)
      else :
        print("틀렸어요.")
        print(stages[userlife])
        userlife -= 1


    if not "_" in blankword :
      print(f"대단해요! 당신은 {startcount-finalcount}회만에 성공했네요. 축하합니다. ")
      end_of_game = True
    
    if userlife == 0 :
      end_of_game = True
      print(stages[userlife])
      print("당신은 실패해습니다.")
 # 알파벳 뽑기
import string
low_letter_list = list(string.ascii_lowercase)

# logo
logo = '''
  ### #     #####  ### ##    #####     ##### ## ###              ### #    ##  #  ## ###   ###       ### ##  ## ###   
 ## ##     ## ##  ##  ##   ##   #     ## ##   ##  ##            ## ##    # ###    ##  ##   ## ##   ##  ##    ##  ##  
###       ##  ##   ##       ####     ##  ##   #   ##           ###         ##     #   ##   ### ##   ##       #   ##  
 ##       ######   ####        ###   ######   ##  ##            ##         ##     ##  ##  ###  ##   ####     ##  ##  
###  #    ##  ##   ##         # ##   ##  ##   ## ##            ###  #      ##     ## ##    ##  #    ##       ## ##   
 ##  ##   ##  ##  ###  ##  ### ###   ##  ##   ## #              ##  ##    ###     ##      ##   #   ###  ##   ## #    
  ####   ##    ## # ####   # ###    ##    ## ###  ##             ####    #   ##  ## ##    ##  #### # ####   ###  ##  
                                                   ##                                                             ## 

'''

# print(low_letter_list)

# logo 출력
print(logo)

# 프로그램 실행
restart_q = "yes"

# 암호화 함수
def caesar(text, shift, direction):
    s_text = text
    text = list(text)
    new_word = ""
    f_shift = shift % 26  # 26이상의 큰수를 입력해도 나머지를 처리하여 알맞은 인수값을 처리할 수 있음.

    if direction != "encode" and direction != "decode":
        print("encode 또는 decode를 정확히 입력해 주세요")
        return

    if direction == "decode" :
        f_shift = f_shift * -1

    for letter in text :
        start_index = low_letter_list.index(letter) #철자별로 알파벳 리스트의 인덱스 값을 찾는다.
        new_index = start_index + f_shift
        if new_index > 26: #알파벳의 끝에 가까울 경우 인덱스 범위를 초과하는 경우가 발생하므로, 알파벳 총 갯수에서 다시 앞의 인덱스에서 알파벳을 찾도록 연산과정 입력
            new_index = f_shift - (26 - start_index)
        new_word += low_letter_list[new_index] #new_word 변수에 알파벳 리스트에서 키 값을 더한 인덱스 위치의 알파벳을 찾아 더한다. 
    print(f"입력한 글자 : {s_text} , {direction} 글자 : {new_word} , 암호키 : {abs(shift)}")
    return

# 프로그램 실행
while restart_q == "yes" :
    user_direction = input("암호화를 하려면 'encode' 를 입력하고, 암호를 해제하려면 'decode'를 입력해 주세요. ").lower()
    user_text = input("암호화 또는 복호화 할 당신의 메세지를 입력해 주세요. : ").lower()
    key_shift = int(input("암호화 또는 복호화 키를 숫자로 입력해 주세요. "))

    caesar(text=user_text, shift=key_shift, direction=user_direction)

    restart_q = input("프로그램을 다시 실행하길 원하시면 'yes'를 입력하고 그렇지 않으면 'no'를 입력해 주세요.").lower()

print("Good Bye")
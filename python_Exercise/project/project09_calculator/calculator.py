from art import logotext

print(logotext)

#더하기
def add(n1, n2):
    return n1 + n2

#빼기
def subtract(n1, n2):
    return n1 - n2

#곱하기
def multiply(n1, n2):
    return n1 * n2

#나누기
def divide(n1, n2):
    return n1 / n2

#연산 딕셔너리
#연산기호에 따라 함수를 값으로 연결
operation = {
"+":add,
"-":subtract,
"*":multiply,
"/":divide
} 

def calculator():
    num1 = float(input("첫번째 숫자를 입력해 주세요. :"))
    for symbol in operation:  #operation 딕셔너리에서 for 반복문으로 키값 출력
        print(symbol)
    should_continue = True

    while should_continue :
        operation_symbol = input("계산할 연산 기호를 입력해 주세요. :")
        num2 = float(input("다음 숫자를 입력해 주세요. :"))
        #operation 딕셔너리에서 해당 연산기호의 함수이름을 calculation_function에 입력
        calculation_function = operation[operation_symbol]
        #calculation_function에 입력된 숫자 두개(num1, num2)추가하여 answer변수에 저장
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        re_continue = input("이어서 계산할까요? 예 = y , 다시 시작 = n ")
        if re_continue == "y" :
            num1 = answer
        else:
            should_continue = False
            calculator() #자신의 함수를 다시 호출하여 새로운 계산을 할 수 있도록 함
            

calculator()
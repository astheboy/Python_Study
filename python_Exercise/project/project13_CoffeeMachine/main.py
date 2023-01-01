from data import menu, resources

# 사용법 안내

def machine_usage_method():

    return f'''
    1. 먹고 싶은 커피를 선택하고 돈을 넣으면 해당 커피를 뽑아줍니다.
    2. 금액이 부족하면 다시 커피를 선택해야 합니다.
    3. 커피 머신의 물, 우유, 커피 양이 부족하면 잠시 후 다시 시도하셔야 합니다.
    4. 'report'를 입력하면 현재 커피 머신의 상태를 알 수 있습니다.
    5. 'no'를 입력하면 커피머신을 정지합니다.
    
    '''
# 현재 커피머신 레포트 출력(물의 양, 커피양, 우유양, 보관 된 동전 금액)
def report_print(resources):
    
    return f'''
    현재 커피 머신 재료 상태
    물의 양 : {resources["water"]}g
    우유 양 : {resources["milk"]}g
    커피 양 : {resources["coffee"]}g
    보관 현금 : {resources["save_money"]}원
    '''

# 커피머신 양이 부족하면 물의 양, 우유 양, 커피 양 채우기
def check_resources(resources, resource):
    if resource == "water":
        resources[resource] = 300
    elif resource == "milk" :
        resources[resource] = 200
    else:
        resources[resource] = 100
    print(f"{resource}가 부족합니다. 잠시 후 다시 해주시기 바랍니다.")
    
    return resources

# 사용자가 원하는 커피를 만들기 위해 커피머신의 재료를 기준에 맞게 조합하고 사용한 재료의 양을 빼기
def coffee_make(menu, select_coffee, resources):
    
    resources["water"] = resources["water"] - menu[select_coffee]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - menu[select_coffee]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - menu[select_coffee]["ingredients"]["coffee"]

    return resources

def exchange_cacl(menu, select_coffee, sum):
    if sum >= menu[select_coffee]["cost"]:
        
        coffee_make(menu, select_coffee, resources)

        exchange = sum - menu[select_coffee]["cost"]
        print(f"거스름돈은 {exchange}원 입니다.")
        print(f"{select_coffee} 맛있게 드세요.")
        resources["save_money"] += menu[select_coffee]["cost"]

    else:
        print("비용이 부족합니다.")

# 코인(백원, 천원, 만원) 계산 및 프로그램 실행 함수
def coffee_machine(menu, select_coffee, resources):
    
    coins = [10000, 1000, 100]
    sum = 0
    for coin in coins:
        input_coin = int(input(f"{coin}원을 넣은 갯수 : "))
        sum += input_coin * coin

    if menu[select_coffee]["ingredients"]["water"] > resources["water"] :
        check_resources(resources, "water")
        print(f"거스름돈은 {sum}원 입니다.")
    elif menu[select_coffee]["ingredients"]["milk"] > resources["milk"] :
        check_resources(resources, "milk")
        print(f"거스름돈은 {sum}원 입니다.")
    elif menu[select_coffee]["ingredients"]["coffee"] > resources["coffee"] :
        check_resources(resources, "coffee")
        print(f"거스름돈은 {sum}원 입니다.")
    else:
        exchange_cacl(menu, select_coffee, sum)

    return resources


# 사용자로부터 먹고 싶은 커피 입력받기
machine_on = True

print(machine_usage_method())

while machine_on :
    select_coffee = input("어떤 커피를 마시겠어요? (espresso, latte, cappuccino) : ")
    
    if select_coffee == "report" :
        print(report_print(resources))

    elif select_coffee == "no" :
        machine_on = False
    
    else:
        coffee_machine(menu, select_coffee, resources)

    

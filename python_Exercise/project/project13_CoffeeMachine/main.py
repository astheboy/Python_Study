from data import menu, resources

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
def input_resource(resource):
    """_summary_

    Args:
        resource (_string_): resouces의 water, milk, coffee 요소

    Returns:
        _dictionary_: 부족한 요소의 양을 다시 넣은 후 resources 딕셔너리를 반환
    """
    print(f"{resource}가 부족합니다. 잠시 후 다시 해주시기 바랍니다.")

    if resource == "water" :
        resources[resource] = 300
    elif resource == "milk" :
        resources[resource] = 200
    else:
        resources[resource] = 100
    return resources

# 사용자가 원하는 커피를 만들기 위해 커피머신의 재료를 기준에 맞게 조합하고 사용한 재료의 양을 빼기
def check_resources(menu, select_coffee, resources, resource):
    if menu[select_coffee]["ingredients"][resource] > resources[resource] :
        input_resource(resource)
        
    else:
        resources[resource] = resources[resource] - menu[select_coffee]["ingredients"][resource]
    return resources

# 코인(백원, 천원, 만원) 계산 및 프로그램 실행 함수
def coffee_machine(menu, select_coffee, resources):
    coins = [10000, 1000, 100]
    sum = 0
    for coin in coins:
        input_coin = int(input(f"{coin}원을 넣은 갯수 : "))
        sum += input_coin * coin
    
    if sum > menu[select_coffee]["cost"]:
        check_resources(menu, select_coffee, resources, "water")
        check_resources(menu, select_coffee, resources, "milk")
        check_resources(menu, select_coffee, resources, "coffee")

        exchange = sum - menu[select_coffee]["cost"]
        print(f"거스름돈은 {exchange}원 입니다.")
        print(f"{select_coffee} 맛있게 드세요.")
        resources["save_money"] += menu[select_coffee]["cost"]
    else:
        print("비용이 부족합니다.")
    return resources


# 사용자로부터 먹고 싶은 커피 입력받기
machine_on = True
while machine_on :
    select_coffee = input("어떤 커피를 마시겠어요? (espresso, latte, cappuccino) : ")
    
    if select_coffee == "report" :
        print(report_print(resources))

    elif select_coffee == "no" :
        machine_on = False
    
    else:
        coffee_machine(menu, select_coffee, resources)

    

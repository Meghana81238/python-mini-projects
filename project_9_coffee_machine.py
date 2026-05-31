report={
    "water":500,
    "milk":500,
    "coffee":500,
    }
    

menu={"latte":{"ingredients":{
    "water":200,
    "milk":150,
    "coffee":24,
    },
    "cost":150
    },
    "espresso":{"ingredients":{
    "water":50,
    "coffee":18,
    },
    "cost":100
    },
    "cappuccino":{"ingredients":{
    "water":250,
    "milk":100,
    "coffee":24,
    },
    "cost":200
    }
}

profit=0
def check_resources(coffee_type):
    for item in coffee_type:
        if coffee_type[item]>report[item]:
            print(f"sorry,there is no enough {item}")
            return False
    return True

def process_coins():
    print("please insert coins")
    totat=0
    coins_five=int(input("how many 5rs coins?"))
    coins_ten=int(input("how many 10rs coins?"))
    coins_twenty=int(input("how many 20rs coins?"))
    total=coins_five*5 + coins_ten*10 + coins_twenty*20
    return total

def is_payment_successfull(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global profit
        profit+=coffee_cost
        change=money_received-coffee_cost
        print(f"here is your Rs{change} in change")
        return True
    else:
        print("sorry that's not enough money.money refounded")
        return False    
        
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        report[item]-=coffee_ingredients[item] 
    print(f"here is your {coffee_name}....Enjoy!")      
machine_on=True
while machine_on:
    choice=input("what would you like to have?\n(latte/espresso/cappuccino)")

    if choice=="off":
        machine_on=False
    elif choice=="report":
        print(f"water={report["water"]} ml")
        print(f"milk={report["milk"]} ml")
        print(f"coffee={report["coffee"]} g")
        print(f"money=Rs{profit}")

    else:
        coffee_type=menu[choice]
        print(coffee_type)
        if check_resources(coffee_type["ingredients"]):
            payment=process_coins()
            if is_payment_successfull(payment,coffee_type["cost"]):
                make_coffee(choice,coffee_type["ingredients"])





    

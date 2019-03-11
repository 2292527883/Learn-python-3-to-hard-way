def cheese_and_craclers(chees_count, boxes_of_crackers):#定义函数 cheese_and_craclers
    print(f"You have {chees_count} cheeses !")
    print(f"You have {boxes_of_crackers} boxes of crackers !")
    print("Man that's enough for a party !")
    print("Get a blanket. \n")


print("We can just give function numbers directly:")
cheese_and_craclers(20,30)#给函数赋值 20(chees_count),30(boxes_of_crackers)


print("OR, we can use variables from our script :")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_craclers(amount_of_cheese,amount_of_crackers)#赋值:amount_of_cheese


print("We can evem dp , math insaide too :")
cheese_and_craclers(10+20,5+6)#赋各种值


print("And we can combine the two , variables and math:")
cheese_and_craclers(amount_of_cheese+100,amount_of_crackers+1000)


#从用户输入获取函数数值
print("""
Now ,we can gei it form everone
""")
cheese = input("you have cheese : \n")
boxse = input("you have boxes : \n" )
print("\n")

cheese_and_craclers(cheese,boxse)

# 分支与函数

from sys import exit


def gold_room():  # 放满金币的房子 选择取多少,非数字结束游戏 是数字 小于50夸奖,大于50批评
    print("This is full of gold .How muck do you take?")

    choice = input("?")
    if"0"in choice or"1"in choice:
        how_much = int(choice)
    else:
        dead("Man,learn to type a number.")
    if how_much < 50:
        print("Nice ,you're not greedy you !")
        exit(0)
    else:
        dead("You greedy bastrad")


def bear_room():
    print("There is a bear here .")  # 一只熊在这
    print("he bear has a bunch of honey")  # 他有一堆蜂蜜
    print("The fat bear is in front of another door")  # 熊在其他门前面
    print("How are you going to move the bear?")  # 你打算如何移动熊?
    bear_moved = False

    while True:  # 任何时候都进入循环
        choice = input(">")  # 获取输入

        if choice == "take honey":  # 拿走蜂蜜
            # 熊看见你并给了你一耳光
            dead("The bear looks at you then slaps Your face off")
        elif choice == "taunt bear" and not bear_moved:  # and (not bear_moved)
            # not bear moved == True
            print("The bear has moved form the door.")  # 熊离开了门
            print("You can gou through it now")
            bear_moved = True  # 熊离开了 True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews you leg off")
        elif choice == "open door"and bear_moved:
            gold_room()
        else:
            print("I got no idea that that means .")


def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it , whatever stares at you and you go insane.")
    print("Do you flee for you life or ear you head?")

    choice = input("?")
    if"flee"in choice:
        start()
    elif "head"in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()


def dead(why):  # 每个函数的结局传入 并打印,退出程序
    print(why, "good job")
    exit(0)


def start():
    print("You are in dark room.")
    print("There is a door to your right and left")
    print("Which one do you take ?")
    choice = input(">")

    if choice == "left":  # 选择为left 进入bear_room 函数
        bear_room()
    elif choice == "right":  # 选择为left 进入cthulhu_room 函数
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")  # 开始游戏 选择分支


start()

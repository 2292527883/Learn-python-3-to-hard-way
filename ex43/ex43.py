
"""
外星人:Alien           迷宫:Maze
玩家:Player           房间:Room
飞船:Ship             场景:Scence
哥顿人:Gothon          死亡:Death
救生舱:Escape Pod      中央走廊:Central Corridor
行星:Planet           激光武器库:Laser Weapon Armory
地图:Map              主控仓:The Bridge
引擎:Engine
"""
# Map: 地图
#   -next_scence    下一个场景
#   -opening_scence     打开场景
# Engine:    引擎
#   -play   开始
# Scence:   场景
#   Enter   进入场景
#   Death   死亡场景
#   Central Corridor    中央走廊
#   Laser Weapon Armory     激光武器库
#   The Bridge  主控仓
#   Escape Pod  救生舱

from random import randint  # 随机数
from sys import exit  # 退出
from textwrap import dedent


class Scence(object):
    # 场景
    def enter(self):
        print("This Scence is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):
    # 引擎

    def __init__(self, Scence_map):
        self.Scence_map = Scence_map

    def play(self):
        # 实例化class(map).open/next scence
        current_sence = self.Scence_map.opening_scence()
        last_sence = self.Scence_map.next_scence('finished')

        while current_sence != last_sence:
            next_scence_name = current_sence.enter()
            current_sence = self.Scence_map.next_scence(next_scence_name)

        # be sure to print out  the last scence
        current_sence.enter()


class Death(Scence):
    quips = [
        "You died. you kinda suck at this",
        "You mom would be proud ..... if she were smarter",
        "such a luser",
        "I have a smaill puppy that's better at this",
        "You're worse than your Dad's Jokes ."
    ]

    def enter(self):
        # 随机打印一句死亡
        print(Death.quips[randint(0, len(self.quips) - 1)])
        pass  # 死亡


class Central_Corridor(Scence):
    # 中央走廊
    if action == "shoot!":
        def enter(self):
            print(dedent("""
            Quick on the draw you yank out your blaster and
            fire it at the Gothon . His clown costume is flowing and
            moving around his body , Which throws off your aim.
            Your laser hits his costume but miss him entirely.
            This completely ruins his brand new costume his mother
            bought him which makes him fly into an insane rage and blast you
            repeatedly in the face until you are dead , then he eats you
            """))
        return 'Death'
    elif action == "dodge!":
        print(dedent("""
        Like a world class boxer you dodge , weabe ,slip and
        slide right as the Gothon;s blaster cranks a laser
        past your head , In the middle of you artful dodge your foot slips and
        you bang your head on the metal wall and pass out . you wake up shortly
        after only to die as the Gothon stops on your head and eats you .
        """))
        return 'Death'
    elif action == "tell a joke":
        print(dedent("""
        Lucky for you  they made you learn Gothon insults in the academy , You
        yell the one Gothon jjoke you know: ;anje znhire vf fb sng ,jura fur
        fvgf nebhaq gur ubhr,  The Gitgib stios m tgies 
        """))


class Laser_Weapon_Armory(Scence):
    def enter(self):
        pass  # 激光武器库


class The_Bridge(Scence):
    def enter(self):
        pass  # 主控仓


class Escape_Pod(Scence):
    def enter(self):
        pass  # 救生舱


class Map(object):
    """docstring for Map."""

    def __init__(self, start_scence):
        pass

    def next_scence(self):
        pass

    def opening_scence(self):
        pass  # 地图


a_map = Map('Central_Corridor')
a_game = Engine(a_map)
a_game.play()

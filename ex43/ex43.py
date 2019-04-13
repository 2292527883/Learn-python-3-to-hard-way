
"""
外星人:Alien           迷宫:Maze
玩家:Player           房间:Room
飞船:Ship             场景:scene
哥顿人:Gothon          死亡:death
救生舱:Escape Pod      中央走廊:Central Corridor
行星:Planet           激光武器库:Laser Weapon Armory
地图:Map              主控仓:The Bridge
引擎:Engine
"""
# Map: 地图
#   -next_scene    下一个场景
#   -opening_scene     打开场景
# Engine:    引擎
#   -play   开始
# scene:   场景
#   Enter   进入场景
#   death   死亡场景
#   Central Corridor    中央走廊
#   Laser Weapon Armory     激光武器库
#   The Bridge  主控仓
#   Escape Pod  救生舱

from random import randint  # 随机数
from sys import exit  # 退出
from textwrap import dedent


class scene(object):
    # 场景
    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):
    # 引擎

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):

        # 实例化class(map).open/next scene
        current_scene = self.scene_map.opening_scene()
        last_sence = self.scene_map.next_scene('finished')

        while current_scene != last_sence:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out  the last scene
        current_scene.enter()


class Death(scene):
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
        exit(0)


class Central_Corridor(scene):
    # 中央走廊
    def enter(self):
        print(dedent("""
            The Gothons of planet Percal #25 haveinvaded your ship and
			desteoyed your entire crew.You are the last surviving
			member and your last mission is to get the neutron destruct
			bomb from the Weapons Armory, put it in the bridge, and
			blow the ship up afther getiing into an escape pod .

			You're running down the central corridor to the Weapons
			Armory when a Gothon jumps out , red scaly skin, dark grimy
			filled body . He's blocking the door to the Armory and
			about topull a weapon blast you.
            """))
        action = input(">")
        if action == "shoot":
            print(dedent("""
                        Quick on the draw you yank out your blaster and
                        fire it at the Gothon . His clown costume is flowing and
                        moving around his body , Which throws off your aim.
                        Your laser hits his costume but miss him entirely.
                        This completely ruins his brand new costume his mother
                        bought him which makes him fly into an insane rage and blast you
                        repeatedly in the face until you are dead , then he eats you
                        """))
            return 'death'
        elif action == "dodge":
            print(dedent("""
                    Like a world class boxer you dodge , weabe ,slip and
                    slide right as the Gothon;s blaster cranks a laser
                    past your head , In the middle of you artful dodge your foot slips and
                    you bang your head on the metal wall and pass out . you wake up shortly
                    after only to die as the Gothon stops on your head and eats you .
                    """))

            return 'death'
        elif action == "tell a joke":
            print(dedent("""
                    Lucky for you  they made you learn Gothon insults in the academy , You
                    yell the one Gothon jjoke you know: ;anje znhire vf fb sng ,jura fur
                    fvgf nebhaq gur ubhr,  The Gitgib stios m tgies
                    """))
            return 'laser_weapon_armory'
        else:
            print("Dose not compute ")
            return 'central_corridor'


class Laser_Weapon_Armory(scene):
    def enter(self):
       # 激光武器库.
        print(
            dedent("""
            you do a dive roll into the wepon armory,crouch and scan
            the room for more gothons that might be hiding, it's dead
             quietm too quiet , you stand up and run the far side of
            the room and find the neutron bomb in its container.
            There's a kepad lock on the box and you need  the code to
             get the bomb out . if you get tge cide woring 10 times the
             the lock closes forever and you can;t get the bomb , the
             code is 3 digits
            """))
        code = 100  # {randint(1, 9)}{randint(1, 9)}{randint(1, 9)}
        guess = input("[keypad]>")
        guesses = 0
        guess = int(guess)
        while guess != code and guesses < 10:
            print("BZZZZZEDDDDD!")
            guesses += 1
            guess = input("[keypad]>")
        if guess == code:
            print(dedent("""
            the container clicks open ande the seal breaks ,letting
            gass out , you grab the neutron bomb and run as fast as
            you can to the bridge where you must place it in the
            right spot.
            """))
            return 'the_bridge'
        else:
            print(dedent("""
            the lock buzzes one last time and then you hear a
            sickening melting soud as the mechanism is fused
            together . you decide to sit there m and finally the
            gothons blow up the ship from their ship and you die.
            """))
            return 'death'


class The_Bridge(scene):
    def enter(self):
        # 主控仓
        print(dedent("""
        You burst on to the bridge with the neron destruct bomb
        undder you arm and surprise 4 gothons who  are trying
        take control of the ship ,each if them hass an even uglier
        weapons out yrt msas they ssee the active bomb uder you
        arn abd diblt want to sset it off
        """))
        action = input(">")
        if action == "throw the bomb":
            print(dedent("""
            in a panic you throw the bomb at the group of gothons
            and make a leao fir the door , right as you drop it a
            Gothon shoots you right in the back killing you .
            as you die you see another gothon frantically try to
            disarm the bomb , you die konwing they will probable
            blow up wen it gose off
            """))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""
            you point your blaster at the bomb under your arm and
            the gothons put their hands up and start to sweat.
            you inch backward to the door m ioen it , and then
            carefullu place the bomb on the floor , pointing your
            blaster at it , you then jump back through the door,
            pinch the close buttin and blast the lock sso Gothons
            canlt get out , now that ,the bomb is placed you run to
            the escape pod to get off this tin can.
            """))
            return 'escape_pod'
        else:
            print("Dose not compuer")
            return "the_bridge"


class Escape_Pod(scene):
    def enter(self):
        # 救生舱
        print(dedent("""
        upi rish through the ship desperatelu trying to make it to
        the escape pod before the whole ship explodes , it sseems
        like hardlu any gothons are on the ship , so your run is
        clear of inter feremce . you get to the chamber with the
        escape pods ,  and now neesd to pick one to take , some
        of them could be damaged but you don;t habe time to look
        there's 4pods , which one do you take ?
        """))
        good_pod = 3  # randint(1, 5)
        guess = input("[pod #]>")
        guess = int(guess)
        if guess != good_pod:
            print((dedent(f"""
            you jump into pod {guess} and hit the eject button,
            the bod esscapes out into the void of space ,then
            implodes as the hull ruptures ,crusshing your body
            into jam jelly.
            """)))
            return 'death'
        else:
            print(dedent("""
            you jump in to pod {guess} and hit the eject button.
            the pod easily slides out into space heading to
            the planet below , as it flies to the planet below, you look
            back and see your ship implode then explode like a 
            bright star , taking out the Gothon ship at the same t
            time , you won!
            """))
            return 'finished'


class Finished(scene):
    def enter(self):
        print("you won ! good job.")
        return 'finished'


class Map(object):
    """docstring for Map."""
    scene = {
        'central_corridor': Central_Corridor(),
        'laser_weapon_armory': Laser_Weapon_Armory(),
        'the_bridge': The_Bridge(),
        'escape_pod': Escape_Pod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scene.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

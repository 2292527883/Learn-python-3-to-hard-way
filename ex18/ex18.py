# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 =args
    print(f"arg1 : {arg1},arg2 : {arg2}")

# ok, that *args is carually pointless,we can just do this
def print_two_again(arg1,arg2):
    print(f"arg1 : {arg1} ,arg2 : {arg2} ")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1} ")

# this one takes no arguments
def print_none():
    print("I'm going nothing'.")


print_two("FUCK","Me")
print_two_again("zed","shaw")
print_one("First!")
print_none()

# while 循环
i = 0  # i赋初值
numbers = []  # 定义一个numbers的空列表

while i < 6:  # 每次循环+1 当i=6时停止运行
    print(f"At the top i is {i}")  # 这是第i次循环
    numbers.append(i)  # 向numbers最后一个元素赋i的值

    i = i + 1  # 每次循环i自增1
    print("Numbers now:", numbers)  # 现在的列表:
    print(f"At the bottom i is {i}")  # 现在i的值


print("The numbers :")

for num in numbers:
    print(num)

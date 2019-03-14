ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list . Let's fix that ")

stuff = ten_things.split(" ")  # 以空格风格字符串存储到stuff变量中
more_stuff = ["Day", "Night", "Song",
              "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:  # 如果stuff的字符串不多于10
    # 移除more_stuff列表中最后一个元素,并将该元素赋值给next_one
    next_one = more_stuff.pop()
    print("Ading : ", next_one)
    # 向stuff列表中第一个空值赋值
    stuff.append(next_one)
    # 打印当前stuff列表中的元素个数
    print(f"There are {len(stuff)} item now .")

print("There we go : ", stuff)

print("Let's do some things with stuff")  # 现在让我们在stuff列表中做一些事

print(stuff[1])  # 打印第二个元素
print(stuff[-1])  # 最后一个元素
print(stuff.pop())  # 打印最后一个元素并删除
# 以" "连接stuff列表中的元素
print(' '.join(stuff))  # 用于将序列中的元素以指定的字符连接生成一个新的字符串。
# 以"#"连接stuff列表的第4到6个元素(不包括6(也就是4,5两个元素))
print('#'.join(stuff[3:5]))

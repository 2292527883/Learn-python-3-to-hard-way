from sys import argv
script, filename = argv
print(f"We're going to erase {filename} ")  # 我们要编辑的文件是:{filename}
print("If you don't want that , hit CTRL-C (^C) . ")  # 如果你不想编辑他 请输入CTRl^c
print("If you do want that ,hit RETURN")  # 如果你要编辑它,请回车

input("?")

print("opening the file...")  # 打开文件中
target = open(filename, 'w')  # 以读写模式打开文件{filename}并赋给target变量

print("Truncating the file . Good bye!")  # 清空文件

target.truncate()  # 清空 文件中的内容

line1 = input("line 1 :")  # 输入第一行内容
line2 = input("line 2 :")  # 输入第二行内容
line3 = input("line 3 :")  # 输入第三行内容和
print("I'm going to write these to the file")  # 正在写入文件

target.write(line1)  # 写入第一行内容 下同
target.write("\n")  # 换行
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finlly , We close it .")

target.close()  # 退出文件

print("下面将打开文件")
txt = open(filename)
print(txt.read())

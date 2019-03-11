# 函数和文件
from sys import argv  # 从外部获取参数 input_file
script, input_file = argv


def print_all(f):  # 作用 :从开头读取文件
    print(f.read())


def rewind(f):  # seek作用:跳转到文件的第一个字节而不是第一行
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)  # 将文件打开到current_file
print("First let's print the whole file :\n")  # 打印文件内容

print_all(current_file)  # 打印文件 同print_all(current_file.read())
print("Now let's rewind , kind of like a tape")
rewind(current_file)  # 将指针调整到第一个字节
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)  # 格式:(行号,该行内容)
# 打印第current_line行的current_file文件
current_line += 1

print_a_line(current_line, current_file)
# 上同
current_line += 1

print_a_line(current_line, current_file)
# 上同

from sys import argv
script, filename, py1 = argv  # 从外部获取参数 赋值给script ,filename

txt = open(filename)  # 打开 filenmae 文件赋值给txt变量
print(f"Here's your file {filename} :")
print(txt.read())  # 读取txt变量的值
print("script的意思是:", script)
print("Type the filename again :")
file_again = input(">")

txt_again = open(file_again)  # 再读取一遍filename的文件

print(txt_again.read())
py = open(py1)
print(py.read())
# 第一次报错py1 不是字符串,没有read属性
# 最后检查发现写成了print(py1.read())
# 第二次报错UnicodeDecodeError: 'gbk' codec can't decode byte”
# 在网上查找原因是使用了GBK编码的文件名:为中文
# 遂编辑TXT文本中的中文改成英文
# 顺利运行
# 结论:命令行运行要使用一致编码的文字

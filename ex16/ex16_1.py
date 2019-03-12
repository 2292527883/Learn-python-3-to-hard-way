from sys import argv
script, filename = argv

print(f"我们要写入的是 {filename} 文件 ")
write = open(filename, 'w')
write.truncate()
line1 = input("请输入第一行:")
line2 = input("请输入第二行:")
line3 = input("请输入第三行:")

print("正在写入中,请稍后")

write.write(line1 + '\n' + line2 + '\n' + line3 + '\n')
# 要写入多行 使用修饰符+连接字符串
write.close()
write = open(filename)
print("下面是写入文件的内容:")

print(write.read())
print("测试 github用")
print("6666666666666")

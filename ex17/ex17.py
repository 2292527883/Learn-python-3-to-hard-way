from sys import argv
from os.path import exists

script , from_file , to_file =argv

print(f"Copying form {from_file} to {to_file} ")#从form_file文件复制到to_file文件

#we could do these two on one line , how?
in_file = open(from_file) #将from_file 的内容赋给in_file
indata = in_file.read() #读取in_file的内容给indata 相当于一个中间值??

print(f"The input file is {len(indata)} bytes long ") #from_filew内容的长度为

print(f"Dose the output file exist ?{exists(to_file)}")
#exist作用:
#将文件名字符串作为参数 如果存在返回Ture 否则返回Fales
print("Ready, hit RETURN to continue , CTRL ^ C to abort")#abort 终止
input()

out_file = open (to_file , 'w')#以读写模式打开{to_file}并赋值给out_file
out_file.write(indata)#将indata({从form_file})写入out_file({to_file})

print("Alright , all done")#一切完成

out_file.close()
in_file.close()
txt=open(to_file)
print("复制后的文件内容 :",txt.read())

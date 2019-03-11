from sys import argv
script,f_file,t_file=argv #获取要操作的文件名
f=open(f_file) # 打开要复制的文件赋值给f
t=open(t_file,'w') #以读写方式打开
r=f.read()
t.write(r)
exit()

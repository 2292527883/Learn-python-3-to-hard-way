<!-- TOC -->

- [记录并整理python基础的常用函数](#记录并整理python基础的常用函数)
    - [1.1. 打印占位和获取用户输入](#11-打印占位和获取用户输入)
        - [1.1.1. input()](#111-input)
        - [1.1.2. f占位符](#112-f占位符)
    - [1.2. 引入模块](#12-引入模块)
    - [1.3. 文件的读写](#13-文件的读写)
    - [1.4. 函数的整理](#14-函数的整理)
        - [1.4.1. strip():根据返回值是ture还是false决定保留还是删除该元素,用来去除换行](#141-strip根据返回值是ture还是false决定保留还是删除该元素用来去除换行)
        - [1.4.2. encode():以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。](#142-encode以-encoding-指定的编码格式编码字符串errors参数可以指定不同的错误处理方案)
        - [1.4.3. format:格式化字符串](#143-format格式化字符串)
        - [1.4.4. split(): 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num+1 个子字符串](#144-split-通过指定分隔符对字符串进行切片如果参数-num-有指定值则仅分隔-num1-个子字符串)
        - [1.4.5. sorted(str):将字符串以Asscii码进行降序排序](#145-sortedstr将字符串以asscii码进行降序排序)
        - [1.4.6. pop(num):一处列表中的一个元素是(默认为最后一个(-1))并返回是删除的元素](#146-popnum一处列表中的一个元素是默认为最后一个-1并返回是删除的元素)
        - [1.4.7. range(num,num)](#147-rangenumnum)
        - [1.4.8. append(obj) /in list/:向列表末尾添加元素](#148-appendobj-in-list向列表末尾添加元素)
        - [1.4.9. len(str):量取字符串长度](#149-lenstr量取字符串长度)
        - [1.4.10. str.join(sequence):用于将序列中的元素以指定的字符连接生成一个新的字符串](#1410-strjoinsequence用于将序列中的元素以指定的字符连接生成一个新的字符串)
        - [1.4.11. 字典的格式:](#1411-字典的格式)
        - [1.4.12. get() :返回指定key的值,如志不在字典中返回默认值](#1412-get-返回指定key的值如志不在字典中返回默认值)
        - [1.4.13. capitalize():将字符串的第一个字母大写,其他字母小写](#1413-capitalize将字符串的第一个字母大写其他字母小写)
        - [1.4.14. count():用于统计字符串里摸个字符出现的次数,可选参数为在字符串搜索的的开始月结束位置.](#1414-count用于统计字符串里摸个字符出现的次数可选参数为在字符串搜索的的开始月结束位置)
        - [1.4.15. replace():把字符串中old字符串替换成new字符串,如果指定第三个max参数,啧替换不超过max次](#1415-replace把字符串中old字符串替换成new字符串如果指定第三个max参数啧替换不超过max次)
        - [1.4.16. try-except方法:](#1416-try-except方法)

<!-- /TOC -->
# 记录并整理python基础的常用函数
## 1.1. 打印占位和获取用户输入
### 1.1.1. input()
- 获取用户输入
- 用法:
- a=input()
- 可使用input("")
- 在""内提示需要输入的参数
### 1.1.2. f占位符
- 用法:
- print函数在引号前加一个f,在""中以一个{}占位
- - 用法

        a=1000
        print(f"the number = {a}")
    输出结果:
        the nimber = 1000
## 1.2. 引入模块
        from sys import argv
            script,a=argv
- 作用:从外部获取参数
- 用法: 
- - 命令(如python)打开文件 (文件名)+参数
  - - 如: python test.py 1
  - - 意义为:用python.exe打开test.py文件,并将1赋给变量a
## 1.3. 文件的读写
open函数
*使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。*
- 用法
- a=open(1.txt,'w')
- 作用:以读写方式打开1.txt ,将内容赋值给a
- w:读写 r:只读
truncate函数
- 清空文件内容
- 用法:
- a.truncate或者truncate(a)
read()
- 用法: a.read()
- 读取a文件(1.txt)
write()
- 向文件中写入字符串
- 用法:
- a.write(someting)
close()
- 关闭文件
  a.close()

示例:

        file=open(a.txt,"w+")#打开文件
        file.read()#读取文件
        file.truncate#清空文件内容
        file.write(somthing+\n+somting2)
        #写入可以用+连接 \n换行
        file.cloes()
---
## 1.4. 函数的整理
### 1.4.1. strip():根据返回值是ture还是false决定保留还是删除该元素,用来去除换行
### 1.4.2. encode():以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
- 语法:str.encode(encoding='utf-8',errors='strict')
### 1.4.3. format:格式化字符串
方法通过字符串中的花括号 {} 来识别替换字段 replacement field，从而完成字符串的格式
- 实例:

        "{}{}".format("hello","world!")
        # 不设置位置,按默认排序 
        结果: 'hello world!'
        # 设置指定位置
        "{0}{1}".format("hello","world")
        结果: hello word!
        可以:"{1}{0}{1}".format("hello","word")
        结果: "world hello world"
``` 
也可以设置参数:

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 >>print("网站名：{0}, 地址 {1}".format('菜鸟教程','www.runoob.com'))
  
通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
  
通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是可选的
```
### 1.4.4. split(): 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num+1 个子字符串
- - 语法：
str.split(str="", num=string.count(str))
参数
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有。
```
实例:
str = "this is string example....wow!!!"
print (str.split( )) # 以空格为分隔符
print (str.split('i',1)) # 以 i 为分隔符
print (str.split('w')) # 以 w 为分隔符
结果:
['this', 'is', 'string', 'example....wow!!!']
['th', 's is string example....wow!!!']
['this is string example....', 'o', '!!!']
```
### 1.4.5. sorted(str):将字符串以Asscii码进行降序排序
### 1.4.6. pop(num):一处列表中的一个元素是(默认为最后一个(-1))并返回是删除的元素
### 1.4.7. range(num,num)
- 创建一个整数列表,一般用在循环中,但是它不是一个真正意义上的列表,它只是在迭代的情况下返回指定索引值
- 但是它不会在内存中真正产生一个列表对象,这样也是为了节约内存空间
- range(0,5):0,1,2,3,4共五个数
从第一个到最后一个数名单不会包含最后一个
### 1.4.8. append(obj) /in list/:向列表末尾添加元素
```
实例:
aList = [123, 'xyz', 'zara', 'abc'];
aList.append( 2009 );
print "Updated List : ", aList;
```
```
结果:
Updated List :  [123, 'xyz', 'zara', 'abc', 2009]
```
### 1.4.9. len(str):量取字符串长度
### 1.4.10. str.join(sequence):用于将序列中的元素以指定的字符连接生成一个新的字符串
- 语法:str.join(sequence)
- - sequence: 要链接的元素序列
- 返回值:返回通过指定字符链接序列中元素后生成新的字符串

```
实例:
s1 = "-"
s2 = "`"
#字符串序列
seq=("r","u","n","n","o")
print(s1.join(seq))
print(s2.join(seq))
```
```
结果:
r-u-n-n-o
r`u`n`n`o
```
### 1.4.11. 字典的格式:
name =  {
        key1:value1
        key2:value2
        key3:value3
}
### 1.4.12. get() :返回指定key的值,如志不在字典中返回默认值
- 语法:dict.get(key,default=None)
        key:要查找的key
        default:如果指定key不存在,返回default(默认值:None)
- - get(key,No find)
### 1.4.13. capitalize():将字符串的第一个字母大写,其他字母小写

- 语法:str.capitalize()
- 返回值:一个首字母大写的字符串
```
实例
以下实例展示了capitalize()方法的实例：

!/usr/bin/python3

str = "this is string example from runoob....wow!!!"

print ("str.capitalize() : ", str.capitalize())
```
```
以上实例输出结果如下：

str.capitalize() :  This is string example from runoob....wow!!!
```
- 需要注意的是：

1、首字符会转换成大写，其余字符会转换成小写。

2、首字符如果是非字母，首字母不会转换成大写，会转换成小写。
### 1.4.14. count():用于统计字符串里摸个字符出现的次数,可选参数为在字符串搜索的的开始月结束位置.
- 语法:str.count(sub,start=0,end=len(string))
        sub:搜索的子字符串
        start:搜索的开始位置,默认为第一个字符[0]
        end:字符串结束搜索的位置,默认为最后一个位置
- 返回值:子字符串在字符串中出现的次数
### 1.4.15. replace():把字符串中old字符串替换成new字符串,如果指定第三个max参数,啧替换不超过max次
- 语法:str.replace(old,new,max)
- 参数:
        old:需要被替换的字符串
        new:替换后的字符串
        max:替换次数不超过max次
- 返回值:替换后的新字符串

### 1.4.16. try-except方法:
- try:运行可能发生错误的语句
        如果出错,返回except的语句


<!-- TOC -->

- [1. 打印占位和获取用户输入](#1-打印占位和获取用户输入)
    - [1.1. input()](#11-input)
    - [1.2. f占位符](#12-f占位符)
- [2. 引入模块](#2-引入模块)
- [3. 文件的读写](#3-文件的读写)
- [4. 函数的整理](#4-函数的整理)
    - [4.1. strip():根据返回值是ture还是false决定保留还是删除该元素,用来去除换行](#41-strip根据返回值是ture还是false决定保留还是删除该元素用来去除换行)
    - [4.2. encode():以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。](#42-encode以-encoding-指定的编码格式编码字符串errors参数可以指定不同的错误处理方案)
    - [4.3. format:格式化字符串](#43-format格式化字符串)
    - [4.4. split(): 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num+1 个子字符串](#44-split-通过指定分隔符对字符串进行切片如果参数-num-有指定值则仅分隔-num1-个子字符串)
    - [4.5. sorted(str):将字符串以Asscii码进行降序排序](#45-sortedstr将字符串以asscii码进行降序排序)
    - [4.6. pop(num):一处列表中的一个元素是(默认为最后一个(-1))并返回是删除的元素](#46-popnum一处列表中的一个元素是默认为最后一个-1并返回是删除的元素)
    - [4.7. range(num,num)](#47-rangenumnum)
    - [4.8. append(obj) /in list/:向列表末尾添加元素](#48-appendobj-in-list向列表末尾添加元素)
    - [4.9. len(str):量取字符串长度](#49-lenstr量取字符串长度)
    - [4.10. str.join(sequence):用于将序列中的元素以指定的字符连接生成一个新的字符串](#410-strjoinsequence用于将序列中的元素以指定的字符连接生成一个新的字符串)
    - [4.11. 字典的格式:](#411-字典的格式)
    - [4.12. get() :返回指定key的值,如志不在字典中返回默认值](#412-get-返回指定key的值如志不在字典中返回默认值)
    - [4.13. capitalize():将字符串的第一个字母大写,其他字母小写](#413-capitalize将字符串的第一个字母大写其他字母小写)
    - [4.14. count():用于统计字符串里摸个字符出现的次数,可选参数为在字符串搜索的的开始和结束位置.](#414-count用于统计字符串里摸个字符出现的次数可选参数为在字符串搜索的的开始和结束位置)
    - [4.15. replace():把字符串中old字符串替换成new字符串,如果指定第三个max参数,则替换不超过max次](#415-replace把字符串中old字符串替换成new字符串如果指定第三个max参数则替换不超过max次)
    - [4.16. try-except方法:](#416-try-except方法)
    - [4.17. 类相关函数:](#417-类相关函数)
        - [4.17.1. issubclass: 检测一个类是否是另一个类的子类](#4171-issubclass-检测一个类是否是另一个类的子类)
        - [4.17.2. isinstance:检测一个对象是否是一个类的实例](#4172-isinstance检测一个对象是否是一个类的实例)
        - [4.17.3. hasattr:检测一个对象是否有成员xxx](#4173-hasattr检测一个对象是否有成员xxx)
        - [4.17.4. getattr():返回一个对象属性值](#4174-getattr返回一个对象属性值)
        - [4.17.5. setattr():返回一个对象属性值](#4175-setattr返回一个对象属性值)
        - [4.17.6. dekattr():用于删除属性](#4176-dekattr用于删除属性)
        - [4.17.7. dir():获取对象的成员列表](#4177-dir获取对象的成员列表)
    - [4.18. 类的成员描述符(property方法):在类中对类的成员属性进行相关操作而创建的一种方式](#418-类的成员描述符property方法在类中对类的成员属性进行相关操作而创建的一种方式)
        - [4.18.1. 使用类实现描述器](#4181-使用类实现描述器)
        - [4.18.2. 使用属性修饰符](#4182-使用属性修饰符)
        - [4.18.3. 使用property函数](#4183-使用property函数)
    - [4.19. 类的内置属性:](#419-类的内置属性)
    - [4.20. 类的常用魔术方法:](#420-类的常用魔术方法)
        - [4.20.1. __init__ : 构造函数:不需要特殊调用,实例化时自动调用](#4201-__init__--构造函数不需要特殊调用实例化时自动调用)
        - [4.20.2. __new__:对象是实例化方法,此魔术方法较特殊,一般不需要使用](#4202-__new__对象是实例化方法此魔术方法较特殊一般不需要使用)
        - [4.20.3. "__call__":当对象作函数使用是触发](#4203-__call__当对象作函数使用是触发)
        - [4.20.4. __str__:当对象被当做字符串时调用,返回一个字符串](#4204-__str__当对象被当做字符串时调用返回一个字符串)
        - [4.20.5. __repr__:返回字符串,同__str__](#4205-__repr__返回字符串同__str__)
    - [4.21. 属性操作相关:](#421-属性操作相关)
        - [4.21.1. __getattr__:访问一个不存在的属性触发:](#4211-__getattr__访问一个不存在的属性触发)
        - [4.21.2. __setattr__ : 对成员属性进行设置时触发](#4212-__setattr__--对成员属性进行设置时触发)
    - [4.22. 运算类相关魔术方法:](#422-运算类相关魔术方法)
        - [4.22.1. __gt__:进行大于判断时触发的函数](#4221-__gt__进行大于判断时触发的函数)
    - [4.23. 类和对象的三种方法](#423-类和对象的三种方法)
    - [4.24. 属性的三种方法:](#424-属性的三种方法)
    - [4.25. 抽象类:](#425-抽象类)
    - [4.26. 自定义类:类其实是一个类定义和各种方法的自由组合](#426-自定义类类其实是一个类定义和各种方法的自由组合)
        - [4.26.1. 自己组装一个类:](#4261-自己组装一个类)
        - [4.26.2. 用type造一个类](#4262-用type造一个类)
        - [4.26.3. 元类的实例:](#4263-元类的实例)

<!-- /TOC -->
记录并整理python基础的常用函数

# 1. 打印占位和获取用户输入
## 1.1. input()
- 获取用户输入
- 用法:
- a=input()
- 可使用input("")
- 在""内提示需要输入的参数
## 1.2. f占位符
- 用法:
- print函数在引号前加一个f,在""中以一个{}占位
- - 用法

        a=1000
        print(f"the number = {a}")
    输出结果:
        the nimber = 1000
# 2. 引入模块
        from sys import argv
            script,a=argv
- 作用:从外部获取参数
- 用法: 
- - 命令(如python)打开文件 (文件名)+参数
  - - 如: python test.py 1
  - - 意义为:用python.exe打开test.py文件,并将1赋给变量a
# 3. 文件的读写
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
# 4. 函数的整理
## 4.1. strip():根据返回值是ture还是false决定保留还是删除该元素,用来去除换行
## 4.2. encode():以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
- 语法:str.encode(encoding='utf-8',errors='strict')
## 4.3. format:格式化字符串
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
## 4.4. split(): 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num+1 个子字符串
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
## 4.5. sorted(str):将字符串以Asscii码进行降序排序
## 4.6. pop(num):一处列表中的一个元素是(默认为最后一个(-1))并返回是删除的元素
## 4.7. range(num,num)
- 创建一个整数列表,一般用在循环中,但是它不是一个真正意义上的列表,它只是在迭代的情况下返回指定索引值
- 但是它不会在内存中真正产生一个列表对象,这样也是为了节约内存空间
- range(0,5):0,1,2,3,4共五个数
从第一个到最后一个数名单不会包含最后一个
## 4.8. append(obj) /in list/:向列表末尾添加元素
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
## 4.9. len(str):量取字符串长度
## 4.10. str.join(sequence):用于将序列中的元素以指定的字符连接生成一个新的字符串
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
## 4.11. 字典的格式:
name =  {
        key1:value1
        key2:value2
        key3:value3
}
## 4.12. get() :返回指定key的值,如志不在字典中返回默认值
- 语法:dict.get(key,default=None)
        key:要查找的key
        default:如果指定key不存在,返回default(默认值:None)
- - get(key,No find)
## 4.13. capitalize():将字符串的第一个字母大写,其他字母小写

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
## 4.14. count():用于统计字符串里摸个字符出现的次数,可选参数为在字符串搜索的的开始和结束位置.
- 语法:str.count(sub,start=0,end=len(string))
        sub:搜索的子字符串
        start:搜索的开始位置,默认为第一个字符[0]
        end:字符串结束搜索的位置,默认为最后一个位置
- 返回值:子字符串在字符串中出现的次数
## 4.15. replace():把字符串中old字符串替换成new字符串,如果指定第三个max参数,则替换不超过max次
- 语法:str.replace(old,new,max)
- 参数:
        old:需要被替换的字符串
        new:替换后的字符串
        max:替换次数不超过max次
- 返回值:替换后的新字符串
## 4.16. try-except方法:
- try:运行可能发生错误的语句
        如果出错,返回except的语句

## 4.17. 类相关函数:
### 4.17.1. issubclass: 检测一个类是否是另一个类的子类
- 语法: issubclasss(class,classinfo)
- 返回值:如果classs是classinfo的子类返回True,否则返回false

### 4.17.2. isinstance:检测一个对象是否是一个类的实例
```
sinstance() 与 type() 区别：

type() 不会认为子类是一种父类类型，不考虑继承关系。

isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。
```
- 语法:isinstance(object,classinfo)
- 参数:
        object:实例对象
        classsinfo:可以是直接或间接类名
- 返回值:如果对象的类型与classinfo的类型相同,返回True,否则返回False
- 实例:
```
>>>a = 2
>>> isinstance (a,int)
True
>>> isinstance (a,str)
False
>>> isinstance (a,(str,int,list)) # 是元组中的一个返回 True
True
```
- type()与isinstance()区别 :
```
class A:
pass
class B(A):
pass
isinstance(A(), A) # returns True
type(A()) == A # returns True
isinstance(B(), A) # returns True
type(B()) == A # returns False
```
### 4.17.3. hasattr:检测一个对象是否有成员xxx
- 语法:hasattr(object,name)<br>
        - objcet:对象<br>
        - name:字符串/属性名
- 返回值:对象有属性返回True,否则返回Flase
### 4.17.4. getattr():返回一个对象属性值
- 语法:getarttr(object,name[,default])
- objcet:对象
name:字符串/属性名
default:默认返回值,如果不提供该参数,在没有对应属性时,触发AttributeErrpr

- 返回值:返回对象属性值
- 实例:
```
>>>class A(object):
... bar = 1
...
>>> a = A()
>>> getattr(a, 'bar') # 获取属性 bar 值
1
>>> getattr(a, 'bar2') # 属性 bar2 不存在，触发异常
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute 'bar2'
>>> getattr(a, 'bar2', 3) # 属性 bar2 不存在，但设置了默认值
3
>>>
```
### 4.17.5. setattr():返回一个对象属性值
- 语法:setarttr(object,name,value)
- 参数:<br>
        objcet:对象<br>
        name:字符串/属性名
        value: 属性值。


- 返回值:无
- 实例:<br>
以下实例展示了 setattr() 函数的使用方法：<br>
对已存在的属性进行赋值：
```
>>>class A(object):
... bar = 1
...
>>> a = A()
>>> getattr(a, 'bar') # 获取属性 bar 值
1
>>> setattr(a, 'bar', 5) # 设置属性 bar 值
>>> a.bar
5
```
如果属性不存在会创建一个新的对象属性,并对属性赋值
```
>>>class A():
... name = "runoob"
...
>>> a = A()
>>> setattr(a, "age", 28)
>>> print(a.age)
28
>>>
```

### 4.17.6. dekattr():用于删除属性
- 语法:
delattr(class,name)
- 返回值:无
### 4.17.7. dir():获取对象的成员列表
- 语法:dir([object])
- 返回值:返回模块的属性列表
实例:
```
>>>dir() # 获得当前模块的属性列表
['__builtins__', '__doc__', '__name__', '__package__', 'arr', 'myslice']
 dir([ ]) # 查看列表的方法
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

```
## 4.18. 类的成员描述符(property方法):在类中对类的成员属性进行相关操作而创建的一种方式

* 类的成员描述符是为了在类中对类的成员属性进行相关操作而创建的一种方式
        - get:获取属性的操作
        - set：修改或添加水属性操作
        - delete：删除属性操作
* 如果想使用类的成员描述符，大概有三种方法
### 4.18.1. 使用类实现描述器
    * __get__
    * __set__
    * __del__
```
实例:
class Student:
    def __init__(self):
        pass


    def __get__(self):
        return self.age
    def __set__(self,age):
        if isinstance(age,int) and  0<age<100:
            self.age=age
        else:
            print("请输入合法的年龄")

stu=Student()

stu.set(110)  #请输入合法的年龄

stu.set(10)

print(stu.get()) #10


```
### 4.18.2. 使用属性修饰符
 * @property
      * @porperty
      * @porperty.setter
      * @porperty,deleter
      * 实例:
```
# ####定义####
class Goods(object):
    
    @property
    def price(self):
        print("@property")
        
    @price.setter
    def price(self, value):
        print("@peice.setter")
        print(value)
        
    @price.deleter
    def price(self):
        print('@price.deleter')
######调用#####
obj = Goods()
# 自动执行@property修饰的price方法，并获取方法的返回值
obj.price
# 自动执行 @price.setter修饰的price方法，并将123赋值给方法的参数
obj.price = 123
# 自动执行@price.delete修饰的price方法
del obj.price     
```
### 4.18.3. 使用property函数
* property(fget,fset,fdel,doc)
  * 参数:
                fget -- 获取属性值的函数
                fset -- 设置属性值的函数
                fdel -- 删除属性值函数
                doc -- 属性描述信息
```
实例:
class c(object):
        def __init__(self):
                self.x=None
        def fget(self):
                return self._x
        def fset(self,value):
                self._x=value
        def fdel(self):
                del self._x
        x = property(fget,fset,fdel,"This is porperty's")
```
* 在c实例化时,x=c(),c.x即将出发getter,c.x=value出发setter,del c.x将触发delete
## 4.19. 类的内置属性:
* 格式:obj.__somethong__
* __dict__:以字典方式显示类的成员组成
* __doc__:获取类的文档信息
* __name__:获取类的名称,如果在模块中使用,获取模块的名称
* __bases__:获取某个类的父类,以元组的方式现实
* 说明文档的格式(__doc__)
```
class some(object):
        '''
        somthing
        '''
        def __init__(self):
                pass

```
print(some.__doc__)

```
结果:
something
```
## 4.20. 类的常用魔术方法:
* 魔术方法就是不需要认为调用的方法,基本是在特定的时刻自动触发
* 统一特征:方法名被前后两个下划线包裹
### 4.20.1. __init__ : 构造函数:不需要特殊调用,实例化时自动调用 
### 4.20.2. __new__:对象是实例化方法,此魔术方法较特殊,一般不需要使用
### 4.20.3. "__call__":当对象作函数使用是触发
```
实例:
class A():
        def __init__(self):
                pass
        def __call__(self):
                print("hello~")
a= A()
a()
```
```
结果:
hello~
```
### 4.20.4. __str__:当对象被当做字符串时调用,返回一个字符串
实例:
```
class A():
        def __init__(self):
                pass
        def __str__(self):
                return "somebody in there"
a= A()
print(a)
```
结果:
```
somebody in there
```
### 4.20.5. __repr__:返回字符串,同__str__
* 语法:repr(object)
* 返回值:返回一个对象的string格式
* 实例:
```
class MyClass() :
    def __str__(self) :
        return "我是MyClass的一个实例"
    def __repr__(self) :
        return "这回连print都省了"
 
a=MyClass()
```
结果:

```
>>> print(a)
我是MyClass的一个实例
>>> a
这回连print都省了
>>> 
```
## 4.21. 属性操作相关:
### 4.21.1. __getattr__:访问一个不存在的属性触发:
实例:
```
Class A():
        name="Noname"
        age = 18
        def __getattr__(self,name):
                print("没找到")
a=A()
print(a.addr)
```
结果:
```
没找到
```
* 这里会多返回一个None,原因不知
* 在csdn找到可能原因:
> 这是因为你定义def red_2():的时候没有显示的使用return 语句，python 解释器会隐式地返回一个 return None

来源:[关于python def函数的打印带None的问题 ](https://bbs.csdn.net/topics/392188067)

### 4.21.2. __setattr__ : 对成员属性进行设置时触发
* 语法:
setattr(object,name,value)
* 参数：
        object--对象
name--字符串，对象属性
value--属性值
* 作用:进行属性设置时经行验证和修改
* 注意:在该方法中不能对属性直接进行赋值操作,否则死循环
* 实例:
```
class A():
        def __init__(self):
                pass
        def __setattr__(self,name,value):
                print("设置属性:{0}".format(name))
                self.name=value
                # 这里又设置一遍属性,会无限递归
                # 为了避免死循环,规定统一调用父类魔法函数
                super().__setattr__(name.value)
a= A()
print(p.__dict__)
p.age=18
```
## 4.22. 运算类相关魔术方法:
### 4.22.1. __gt__:进行大于判断时触发的函数
* 参数:
self
第二个参数时第二个对象
返回值可以时任意值,推荐返回布尔值
* 实例:
  
```
class A():
        def __init__(self,name):
                self._name=name
        def __gt__(self,obj):
                print("{0}会比{1}大吗?".format(self.name,obj.name))
                return self._name > obj._name
a= A()
a1=A("one")
a2=A("tow")
print(a1>a2)
```
## 4.23. 类和对象的三种方法
* 实例方法
        需要实例化对象才能使用的方法,使用过程中可能需要戒指对象的其他对象的方法完成
* 静态方法
        不需要实例化,通过类方法直接访问
* 类方法
        不需要实例化
* 实例:
```
class A():
        #实例方法
        def eat(self):
                print(self)
                print("Eating....")
        #类方法:
        @classmethod
        def play(cls):
                print("Playing)
        #静态方法:
        #不需要第一个参赛数表示自身或者类
        @staticmethod
        def say():
                print("saying")

#实例方法:
yueyu=A()
yueyue.eat()
#类方法:
A.play()
yueyue.play()
#静态方法:
A.say()
yueyue.say()
```
## 4.24. 属性的三种方法:
1. 赋值:
2. 读取
3. 三处
* 实例:
```
class A():
        name="Name"
        pass
a=A()
a.name="someboday"
print(a)
del a.name
```
## 4.25. 抽象类:
* 抽象方法:没有具体实现内容的方法成为抽象方法
* 抽象方法的主要意义是规范了子类的行为和接口
* 抽象类的使用主要借助abc模块
  import abc
* 抽象类:包含抽象方法的类叫抽象类,通常称为ABC类
- 实例:
```
import abc
#生命一个类并制定当前类的元类
class Human(metaclass=abc.ABC.meta):
        #定义一个抽象方法
        @abc.abstractmethod
        def smokiing(self):
                pass
        #定义类抽象方法
        @abc.abstractclassmethod
        def drink():
                pas
        # 定义静态抽象方法
        @ abc.abstractstaticmethod
        def play():
                pass
        def sleep():
        print("sleeping....")
```
* 抽象类的使用:
    * 抽象类可以包含抽象方法,也可以包含具体方法
    * 抽象类中可以有方法也可以有属性
    * 抽象类不能直接实例化
    * 必须继承才可以使用,并且继承的子类必须实现继承来的抽象方法
    * 如果子类没有实现所有继承的抽象方法,子类也不能被实例化
    * 抽象类主要作用是设定类的标准,以便于开发时具有统一的规范
## 4.26. 自定义类:类其实是一个类定义和各种方法的自由组合
* 可以自定义类和函数,然后通过类直接赋值
* 可以借助MethodType实现
* 借助于type
* 利用元类实现 - MetaClass
  * 元类是类
  * 被用来创造别的类
### 4.26.1. 自己组装一个类:
``` 
class A ():
    pass
def say(self):
    print("Saying......)

a.say = say

a= A()

a.say()


--> saying......

```
* 实例2
```
class A():
    pas
def say(self):
    print("saying.......")
    
a=A()
a.say=say
s.say()
# 报错
# 可以绑定类,不能绑定实例
```
解决方法:
```
from types import Methodtype

class A():
    pas
def say(self):
    print("saying.......")
    
a=A()
a.say=methodType(say,A)
# 参数: 实例,类
s.say()
```
### 4.26.2. 用type造一个类
```
#定义类该剧有的成员函数
def say(self):
    print("saying....")
def talf(self):
    print("Talking...")
# 组装类参数:
# type(name,bases,dict)->a new type
# 类名称,父类,组成的各种方法和成员(字典类型)
A=type("Aname",(object,),{"class_say:say","class_talk":talk})
# 然后可以像正常访问一样使用类
a=A()
a.talk()
```
### 4.26.3. 元类的实例:

```
# 元类的写法是固定的,必须继承于type,结尾约定为Metclasss
class someMetclass(type)
    # 注意以下写法
    def __new__(cls,name,bases,attrs):
        ...
        # 自己的业务处理
        attrs["id"]="123456"
        attrs["addr"]="something"
        ...
        return type.__new__(cls,name,bases,attrss)
# 元类定义完就可以使用,注意使用写法
class Teacher(object,metaclass = someMetclasss):
    pass
t=teacher()
t.id
--> "123456"
```
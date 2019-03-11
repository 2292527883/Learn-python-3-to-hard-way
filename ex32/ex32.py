the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'cranges', "pears", "apricots"]
change = [1, 'pennies', 2, 'dimes', 'quarters']
# 二维数组:
count = [[1, 2, 3, 4], [5, 6, 7, 8, 9, 0]]  # 二维数组
print(count)
"""this first kind of for-loop goes through a list"""
for number in the_count:

    print(f"This is count {number}")

"""some as avove"""

for fruit in fruits:
    print(f"A fruit of tyre : {fruits}")

# also we can go through mixed lists too
# notice we have to use () since we dong;t know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists ,frist start with an empty one
elements = []  # 定义elements为一个空列表

# then use the range function do 0 to 5 count
for i in range(0, 5):  # range() 函数可创建一个整数列表，
    # 一般用在 for 循环中。但是它不是一个真正意义上的列表,它只是在迭代的情况下返回指定索引
    # 值，但是它并不会在内存中真正产生一个列表对象，这样也是为了节约内存空间
    # range(0,5) :0,1,2,3,4 共五个数 range()函数会从第一个数到最后一个数名单不会包含最后一个数
    print(f"adding {i} to the list")
    # append is a funtion that lists understand
    elements.append(i)  # 向列表末尾添加元素

# now we can print them ot too
print("I=", i)  # i是一个变量而不是列表,所以只会打印最后一个添加的值:I=4
for i in elements:
    print(f"elements was : {i}")

print(elements)

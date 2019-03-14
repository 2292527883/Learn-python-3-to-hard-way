# 字典

# create a mapping of state to abbreviation
statse = {  # 定义字典
    'Oregon': 'OR',
    'Floida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some citise in them
cites = {
    'CA': 'san Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more citise
cites['NY'] = 'New york'  # 向字典cites 添加 'NY'对应'New york'
cites['OR'] = 'Oregon'

# 打印元素的对应元素
print('-' * 10 * 10)
print("Michigan's abbreviation is :", statse["Michigan"])
print("Floida's abbreviation is :", statse["Floida"])


# do it by using the state then cities dick
print('-' * 100)
# 查找states字典中的michigan对应的元素'MI' 来对应cites 的'Detroit'
print("Michigan has :", cites[statse['Michigan']])
print("Floida's abbreviation is :", cites[statse['Floida']])

# print ever state abbreviation
print('-' * 100)
for state, abbrev in list(statse.items()):
    """
    在该循环中
    state接受 key (密匙/键盘?)的值
    abbrev接受 value(值)的值
    字典(key:value)
    item遍历字典用法:
    for key , value in list#list(dic.items())
    """
    print(f"{state} is abbrevuated {abbrev}")

# print every city in states
print('-' * 100)
for key, value in list(cites.items()):
    print(f"{key} has the city {value}")

# now do both an the same time
print('-' * 100)
for key, value in list(statse.items()):
    print(f"{key} state is abbreviated {value}")
    print('-' * 100)
    print(f"and has city {cites[value]}")

print("-" * 100)
# safely get a abbreviation by state that might not be thers
# get() 函数返回指定键的值，如果值不在字典中返回默认值None。
# 格式:get(指定值,返回值)
statse = statse.get('Texas')

if not statse:  # statse为空值
    print("sorry , no Texas")

# get a citu with a default value
city = cites.get('TX', 'Dose NOt Exist')
print(f"The city for the state 'TX' is {city}")

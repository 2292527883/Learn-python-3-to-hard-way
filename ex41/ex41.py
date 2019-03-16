import random  # 引入以一个名叫random的库 作用:生成随机数
import sys  # 同上
from urllib.request import urlopen  # 从urllib.request中引入urlopen 的库?

WORD_URL = "https://learncodethehardway.org/words.txt"
WORDS = []
PHRASES = {  # 创建以一个叫phrase 的字典
    "class %%%(%%%):":  # 创建以一个叫%%%的类,他是%%%的一种
    "MAKE A calss named %%% that is-a %%%",
    "class %%%(object):\n\tdef_init_(selt,***)":
    # 类%%%里有一个_init_,他接受selt,***作为参数
    "class %%% has a _init_ that takes self and ***params",
    "class %%%(object):\n\tdef ***(self.@@@)":
    # 类%%%有一个函数 *** ,它接受self和@@@为参数
    "class %%% has a function *** that takes self and @@@ params",
    "***=%%%()":
    "set *** to an instance of class %%%",
    # 将***设置为类%%%的一个实例
    "***.***(@@@)":
    # 从 类***调取***函数,使用self和@@@调用它
    "From *** get the *** function , call it with params self ,@@#",
    "***.***='***'":
    # 从 类***中获取 ***属性,并将其设为'***'
    "From *** get the *** attribute and set it to '***'"
}
# do they want to drill phrases first
# 判断:argv的需要的参数是否为两个,且第二个参数是否为'English',是则PHRASE_FIRST=True
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words form the website
# 从web下载文本
for word in urlopen(WORD_URL).readlines():
    # 向列表WORDS中添加以utf-8的格式字符串并在word中删除
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    # capitalize:将w的字符串的首字母大写其他小写
    # 将单词随机排列后赋给class_name
    class_names = [w.capitalize()
                   for w in random.sample(WORDS, snippet.count("%%%"))]
    # 同上
    other_names = random.sample(WORDS, snippet.count("***"))
    # 定义两个空列表
    results = []
    param_names = []
    for i in range(0, snippet.count("@@@")):
        # 将范围是1-3的随机整数赋值给params_count
        param_count = random.randint(1, 3)
        # 向param_names列表添加,和随机的第[param_count]字符串
        param_names.append(','.join(random.sample(WORDS, param_count)))
    for sentence in snippet, phrase:
        # 复制列表的方法
        # 对列表中所有元素进行切片操作
        result = sentence[:]

        # fake class class_names
        for word in class_names:
            # replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)
            # 如果指定第三个参数max，则替换不超过 max 次。
            result = result.replace("%%%", word, 1)

        # fake other class_names
        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    return results

# keep going until thy hit CTRL-D


# try:运行可能发生错误的语句
# 如果出错, 返回except中的语句
try:
    while True:
        # 将字典PHRASES的KEY以列表形式赋给snippets
        snippets = list(PHRASES.keys())
        # 打乱snippets列表的顺序
        random.shuffle(snippets)

        for snippet in snippets:
            # 将value取到phrase中
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            print(snippet)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input(">")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\n BYE")

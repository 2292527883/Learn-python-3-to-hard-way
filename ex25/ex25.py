def break_words(stuff):  # 作用:将字符串以空格的判断条件分割
    """This fution will break up words for Us ."""
    words = stuff.split(' ')  # split作用:将stuff的字符串以(' ')之间的字符分割此处为空格
    return words


def sort_words(words):  # 降序排序
    """sorts the words ."""
    return sorted(words)  # sorted()作用:将字符串进行降序排序


def print_first_word(words):  # 删除并打印第一个字符
    """prints the first word a after popping it off ."""
    word = words.pop(0)  # pop作用:移除列表中的一个元素(默认为最后一个 :-1)并返回删除的元素
    print(word)


def print_last_word(words):  # 删除并打印最后一个字符
    """prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):  # 一次将sentence进行分割,降序排序
    """takes in a full sentence and returns the sortedwords."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):  # 一次将排序后的第一个和最后一个元素删除
    """prints the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sroted(sentence):  # 一次排序 删除第一个和最后一个元素,函数嵌套
    """srots the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

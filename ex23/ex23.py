import sys
script , encoding , error =sys.argv


def main(language_file,encoding,errors):
    line = language_file.readline() #当前行赋给line
    if line: #判断改行是否为空值,是则结束运行
        print_line(line,encoding,errors) #当前行的内容 编码 strict似乎是关键字?
        return main(language_file, encoding,errors) #递归调用


def print_line(line,encoding,errors): #作用:显示字符串和字符
    next_lang = line.strip() #函数的作用是“根据返回值是True还是False决定保留还是丢弃该元素 作用是去除换行
    raw_bytes = next_lang.encode(encoding,errors=errors) #用encode函数进行编码 (UTF-8格式,字符串) 把utf-8格式的字符串编码赋值给raw_bytes
    cooked_string = raw_bytes.decode(encoding,errors=errors) #把utf-8格式的字符串解码赋值给cooked_string

    print(raw_bytes,"<===>",cooked_string,'\n')



languages = open("languages.txt",encoding = "utf-8")#以 utf-8格式打     开languages.txt

main(languages,encoding,error)

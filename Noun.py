import codecs
import nltk
import string
import re
import json
from collections import Counter
from nltk.corpus import stopwords

regex = re.compile('[%s]' % re.escape(string.punctuation))


def read():
    file = codecs.open("Данные для 1 и2 задания.json", "r", "utf_8_sig")                            # файл с словами
    str = file.read()
    file.close()
    return str


def tokenization(my_str):
    pattern = '\"object\":{\"summary\":\".+?\"'                                                     # паттерн поиска
    stop_words = stopwords.words('english')
    object_summary = re.findall(pattern, my_str)
    object_summary = list(map(lambda x: x.replace('"object":{"summary":', ""), object_summary))     #выбор содержимого строки "object":{"summary":'
    tokens = " ".join(object_summary)
    tokens = nltk.word_tokenize(tokens)                                                             #Токенизация
    tokens = list(map(lambda x: regex.sub('', x), tokens))                                          #Удаление пунктуации
    tokens = [i for i in tokens if (i not in stop_words)]                                           #Удаление стоп слов
    tokens = " ".join(tokens)
    count_noun(tokens)


def count_noun(my_str):
    token = nltk.word_tokenize(my_str)
    noun = nltk.pos_tag(token)                                                                      #Определение части речи
    noun = [x[0] for x in noun if x[1] == "NN"]
    noun = Counter(noun)
    noun = {i: noun[i] for i in noun if noun.get(i) > 2}                                            #Формирование словаря Существительное:Количество вхождений
    file = open('task1.txt', 'w')                                                                   #Запись в json  Существительное:Количество
    file.write(json.dumps(noun))
    #print(noun)


if __name__ == "__main__":
    str = read()
    tokenization(str)


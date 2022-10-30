def get_count_char(str_):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for i in str_:
        if i.isalpha():
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
    return dict1

def function (dict_):
    summa = 0
    for number in dict_.values():
        summa += number
    for i in dict_:
        dict_[i] = round(dict_[i]/summa, 3)
    return dict_

dict1 = {}
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(function(dict1))

# 8) В заданной строке расположить в обратном порядке все слова. Разделителями
#    слов считаются пробелы.

text = input("Введите строку:")

for i in text.split(" "):
    print(i[::-1], end=" ")

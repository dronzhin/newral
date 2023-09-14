friends = ['max', 'leo', 'man', 'kate']  # Список друзей

# Функция возвращает последний символ слова
def fff(x):
    return x[-1]


result1 = sorted(friends)  # Сортировка по первой букве
result2 = sorted(friends, key=fff)  # Сортировка по функции (последней букве)
print(type(result2))  # Тип - <class 'list'>
print(list(result1))  # ['kate', 'leo', 'man', 'max']
print(list(result2))  # ['kate', 'man', 'leo', 'max']

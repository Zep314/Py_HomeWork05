# Напишите программу, удаляющую из текста все слова содержащие "абв". 
# Используйте знания с последней лекции. Выполните ее в виде функции. 

# Сначала разбиваем на слова, потом строим новый список на возврат, 
# в котором фильтруем слова с подстрокой "абв"
def CleanABV(local_str): return ' '.join(filter(lambda e: e.find('абв') == -1, local_str.split(' ')))

init_text = 'Вез корабль абв_слово карамель, наскочил мусорное_абв_слово корабль на мель, матросы две недели еще_одно_абв_слово карамель на мели ели.'

print(init_text)
print('========================')
print(CleanABV(init_text))
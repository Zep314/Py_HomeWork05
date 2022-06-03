# Чисто для тренировки новый функций, ничего сложного. 
# Создайте два списка — один с названиями языков программирования, 
# другой — с числами от 1 до длины первого плюс 1. 
# Вам нужно сделать две функции: первая из которых создаст список кортежей, 
# состоящих из номера и языка, написанного большими буквами. 
# Вторая — которая отфильтрует этот список следующим образом: 
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
# то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется. 
# Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. 
# С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc_cost = {alphabet[i]:i+65 for i in range(len(alphabet))}

program_languages = ['Python','C','Fortran','Java','Go','PHP','Pascal','Basic','Lisp','Assembler','Prolog','Perl','Bash']
my_numbers = list(range(1,len(program_languages)+1))

# Вычисляем "стоимость" одного слова
def CostWord(local_str): return sum([abc_cost[local_str[i]] for i in range(len(local_str))])

# Функция 1 для задания
def MyGetTuples(list1,list2): return [(list1[i],list2[i].upper()) for i in range(len(list1))]

# Функция 2 для задания
def MyFilter(local_list): return [list([CostWord(local_list[i][1]),local_list[i][1]]) \
                                  for i in range(len(local_list)) \
                                  if CostWord(local_list[i][1]) % local_list[i][0] == 0]

#print(program_languages)
#print(my_numbers)
print(MyGetTuples(my_numbers,program_languages))
print('===================')
print(MyFilter(MyGetTuples(my_numbers,program_languages)))

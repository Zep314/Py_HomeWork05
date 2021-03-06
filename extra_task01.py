# Супер-сложная.
# Совершенным числом называется число, у которого сумма его делителей равна самому числу. 
# Например, сумма делителей числа 28 равна 1 + 2 + 4 + 7 + 14 = 28, что означает, 
# что число 28 является совершенным числом.
# Число n называется недостаточным, если сумма его делителей меньше n, и называется избыточным, 
# если сумма его делителей больше n.
# Так как число 12 является наименьшим избыточным числом (1 + 2 + 3 + 4 + 6 = 16), 
# наименьшее число, которое может быть записано как сумма двух избыточных чисел, равно 24. 
# Используя математический анализ, можно показать, что все целые числа больше 28123 могут 
# быть записаны как сумма двух избыточных чисел. Эта граница не может быть уменьшена дальнейшим анализом, 
# даже несмотря на то, что наибольшее число, которое не может быть записано как сумма двух избыточных чисел, 
# меньше этой границы.
# Найдите сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных чисел.

# Не такая уж т суперсложная... Вот вторая экстразадача....
import time

def Divisors(n): # возвразаем список делителей числа n
    res = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0: res.append(i); res.append(n//i)
    del res[1] # удаляем n из списка делителей
    return list(set(res))

def IsPerfectNum(n): # Проверка на "Совершенство" числа n
    sum_devs = sum(Divisors(n))
    if sum_devs == n: return 0  # n - Совершенное число
    elif sum_devs > n: return 1 # n - Избыточное число
    else: return -1             # n - Недостаточное число

def GetNo2ExcessNums():
    limit_nums = 28123 # Ну раз математики доказали, что больше чисел не бывает, то верим им
    excess_nums = [ i for i in range(1,limit_nums) if IsPerfectNum(i) == 1 ] # генерируем список избыточных числел
    ret = []
    for i in range(24,limit_nums):  # так же математики доказали, что чисел, меньше 24 тоже не бывает
        for j in excess_nums:
            if not ((i - j) in excess_nums):
                ret.append(i)
                break
    return ret

start_time = time.time()
print(sum(GetNo2ExcessNums()))
print(f'Программа работала {time.time() - start_time} секунд [{time.strftime("%H:%M:%S",time.gmtime(time.time() - start_time))}]')

# Единичная дробь имеет 1 в числителе. Десятичные представления единичных дробей со 
# знаменателями от 2 до 10 даны ниже:

# 1/2=0.5
# 1/3=0.(3)
# 1/4=0.25
# 1/5=0.2
# 1/6=0.1(6)
# 1/7=0.(142857)
# 1/8=0.125
# 1/9=0.(1)
# 1/10=0.1
# Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры. 
# Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.

# Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную
#  повторяющуюся последовательность цифр.

import re
from itertools import groupby

def repeat_inside(text):  
    return "".join(
                    [ s for s, _ in groupby(
                                            list(
                                                max( [x[1] for x in re.findall(r'((\w+)\2+)', text)]
                                                    , key=len
                                                    , default='')
                                                )
                                           )
                    ]
                  )

def MyFind(n):
    ret = {len(repeat_inside(format(1/i,".55"))):i for i in range(2,n)}

    return ret[max([key for key in ret.items()])[0]]

findNUM = MyFind(1000)

print(f'1/{findNUM} = {format(1/findNUM,".55")}, repeat = {repeat_inside(format(1/findNUM,".55"))}')


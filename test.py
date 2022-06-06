# для мелких тестов, не для сдачи задания



# excess_nums = [12, 18, 20, 24, 30, 36, 40, 42, 48]

# import re

# text = '0.001010101010101010100133978042435956012923270463943481445'
# #s = re.findall(r'((\d+)\2+)', text)
# s = re.findall(r'((\d+)\2+)', text)
# print(s)
# text = '10101010'
# s = re.findall(r'((\d+)\2+)', text)
# #print(s)

import re
from itertools import groupby

def my_find_all(text):
    ret = re.findall(r'((\w+)\2+)', text, flags=0)
    ret = max(ret, key= len, default='')
    if ret== '': return ''
    return ret[1]

def rp3(text):
    tmp2 = text
    tmp1 = tmp2
    while tmp2 != '':
        tmp1 = tmp2
        tmp2 = my_find_all(tmp1)
    return tmp1


def repeat_inside(text):  
    # return "".join(
    #                 [ s for s, _ in groupby(
    #                                         list(
    #                                             max( [x[1] for x in re.findall(r'((\w+)\2+)', text)]
    #                                                 , key=len
    #                                                 , default='')
    #                                             )
    #                                        )
    #                 ]
    #               )
    ret = []
    for x in re.findall(r'((\w+)\2+)', text, flags=0):
        ret.append(x[1])
    print(ret)
    ret = max(ret, key= len, default='')
    print(ret)

    # for s in s, _ in groupby(ret):
    #     ret.append(s)
    ret = "".join(ret)
    return ret

#s = '0.001010100133978042435956012923270463943481445'
#s = '0.001010101010101010100133978042435956012923270463943481445'
#s   = '0.0012121212'

s = '0.08333333333333332870740406406184774823486804962158203125'

#s= ''

#print(repeat_inside(s))
print(my_find_all(s))
print(rp3(s))

# print(repeat_inside(repeat_inside(s)))
# print(repeat_inside(repeat_inside(repeat_inside(s))))
# print(repeat_inside(repeat_inside(repeat_inside(repeat_inside(s)))))

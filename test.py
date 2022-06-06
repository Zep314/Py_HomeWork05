# для мелких тестов, не для сдачи задания

excess_nums = [12, 18, 20, 24, 30, 36, 40, 42, 48]

import re

text = '0.001010101010101010100133978042435956012923270463943481445'
#s = re.findall(r'((\d+)\2+)', text)
s = re.findall(r'((\d+)\2+)', text)
print(s)
text = '10101010'
s = re.findall(r'((\d+)\2+)', text)
#print(s)
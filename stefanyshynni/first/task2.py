"""
Дано текст.
Видалити елементи значення integer
"""

text1 = str(input('text:'))
list1 = ','.join(list(text1))
n = 0
if isinstance(list1[n], int):
    list1.remove(str)
    n += 1
print (list1)
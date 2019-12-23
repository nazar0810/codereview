""""
Дано список.
Вивести кількість елементів списку типу string
"""

list1 = list(input('список='))
k = 0
if isinstance(list1[k], str):
    k += 1
print(k)
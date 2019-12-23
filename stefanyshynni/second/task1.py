"""
Написати валідатор для вводу та виводу даних на мові програмування Паскаль
"""

import re
def validator ():
    text = input('Введіть дані:')
    if bool(re.compile('^(Begin){1}\\n writeln{0,+}readln{0,+}(Begin){0,1} writeln{0,+}readln{0,+} end{0,1}\\n end{1}$',text)):
        print ('Yes')
    else:
        print ('no')
        validator()

flag = input('для запуску програми натисніть \"Enter\", щою завершити програми \"n\"')
if flag != 'n':
    validator()
    flag = input('для запуску програми натисніть \"Enter\", щою завершити програми \"n\"')
else:
    print('Допобачення')
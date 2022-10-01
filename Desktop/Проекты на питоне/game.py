"""Игра угадай число"""

from itertools import count
import numpy as np

#Переменная чисто для тренировки работы с версиями
n=99


def random_predict(n1):
    #Переменные, с помощью которого алгоритм будет отгадывать число  максимум за 7 попыток
    l = 1
    r = 100
    #Эта переменная будет применена только в том случае, если выбор сократится до двух чисел.
    #Тогда правильный ответ станет известен независимо от верности текущей попытки.
    d = 0


# количество попыток
    count = 0

    c = 0
    while c!=n1:
        count+=1
        if l==1:
            if (r%2)==0:
                c=int(r/2)
            else:
                c=int(r/2+1)
        else:
            if (r-l)>2:
               c = int(l + (((r-l)/2)+1))
            if (r-l)==2:
                c=l+1
            if(r-l)==1:
                d=1

    
        if c > n1:
            if d==0:
               r=c
            else:
                c=l
                count = count+1   

        if c < n1:
            if d==0:
              l=c
            else:
              c=r
              count = count+1
    return count   

count_ls = []
#np.random.seed(1)  # фиксируем сид для воспроизводимости
random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

for number in random_array:
     count_ls.append(random_predict(number))

score = int(np.mean(count_ls))
print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
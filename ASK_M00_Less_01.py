
           # по условию задачи складываем 1 и 2 число
print(23891471923807487.142352314353455+23891471923843245.142352314334563)
           # по условию задачи складываем 2 и 4 число
print(23891471923807487.142352314356734+23891471923843245.142352314334553)
           # из анализа результата очкевидно,
           # что программа восприняла толко первые 16 цифр
           # вычитаем из 1-го результата 2 результат.
print(23891471923807487.142352314353455-int(23891471923807487.142352314353455))
           # получается 0.0, это подтверждает,
           # что полученные значения в целой часте чисел равны.
           # следовательно анализировать нужно только дробную части.
           # если при решениизадачи операться толко на пройденные материал,
           # то приходится только визуальносравнить вске 4 числа.
           # очевидно, что они различаются только последними 5 цифрами.
           # тогда выделяем 5 последних цифр из кадого числа и складываем их
           # по условию задачи,т.е. 1 с 3
print(142352314353455%100000+142352314334563%100000)
           # по условию задачи, 2 с 4
print(142352314356734%100000+142352314334553%100000)
           #  выводим на печать результата сравнения полученных результатов
           #  по условию задачи
print(88018>91287)
           # получаем логическое  значение "лож",
           # т.е. первый результат мнеьше 2-го.
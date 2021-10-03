money = float(input("Введите сумму в рублях, которую вы планируете положить в банк под проценты"))
money_1 = money/100
a = money_1*5.6
b = money_1*5.9
c = money_1*4.2
d = money_1*4.0
deposit = [a,b,c,d]
import numpy as np
deposit = list(np.around(np.array(deposit),2))
print ("ТКБ||СКБ||ВТБ||СБЕР -",deposit)
print("Максимальная сумма, которую вы можете заработать —", int(max(deposit)),"рублей")
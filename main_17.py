per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму которую хотите внести под проценты:"))
deposit = []
for key in per_cent:
    deposit.append(int(per_cent[key]*money/100))
print(deposit)
max_deposit = max(deposit)
min_deposit = min(deposit)
print(f'Максимальная сумма прибыли с депозита {max_deposit} руб.')
print(f'Минимальная сумма прибыли с депозита {min_deposit} руб.')
print(f'В итоге самый выгадный вклад :{max_deposit} от СКБ со ставкой 5.9%,')
money_capital = 10000   # подушка безопасности
salary = 5000   # зарплата
spend = 6000    # расходы на проживание
increase = 0.05    # рост цен

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение

# зарплата выдается в конце месяца, после месячных трат
new_month = money_capital   # new_month - это сумма, имеющаяся в начале нового месяца
after_spend = 0    # after_spend - это сумма после месячеых трат (перед получением зарплаты)

while new_month > spend:
    after_spend = new_month - spend
    new_month = after_spend + salary
    spend *= (1 + increase)
    month += 1

print(month)

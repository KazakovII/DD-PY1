money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05


def survive(m_c, sal, sp, incr):
    count = 0
    while m_c - spend * (1 + incr * count) > 0:
        m_c = m_c - spend * (1 + incr * count) + sal
        count += 1

    return count


month = survive(money_capital, salary, spend, increase)  # количество месяцев, которое можно прожить

print(month)

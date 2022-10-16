salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен


def survive(sal, sp, m, incr):
    m_c = sp - sal
    for i in range(1, m):
        sp *= (incr+1)
        m_c += sp - sal
    return m_c

need_money = survive(salary, spend, months, increase)  # количество денег, чтобы прожить 10 месяцев

print(round(need_money))

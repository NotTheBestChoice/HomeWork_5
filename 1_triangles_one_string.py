k_list = []
i = 1
i1 = 1
ik = 1
sep = '=' * 50

tr_nums = int(input('Введите количество прямоугольных треугольников, для которых хотите выполнить расчет: '))
print(sep)

while i1 <= tr_nums:
    k_list.append(float(input('Введите поочередно длины катетов для {}-го треугольника: '.format(i1))))
    k_list.append(float(input('И еще разок для второго катета {}-го треугольника: '.format(i1))))
    i1 += 1
print(sep)

while i <= tr_nums:
    k1 = k_list[ik-1]
    k2 = k_list[ik]
    s = k1 * k2 / 2
    c = (k1**2 + k2**2)**0.5
    print(f'Треугольник {i} с катетами {k1} и {k2} имеет площадь {s} и гипотенузу {c}')
    i += 1
    ik += 2
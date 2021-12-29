k1_list = []
k2_list = []
i = 1
i1 = 1
i2 = 1
sep = '=' * 50

tr_nums = int(input('Введите количество прямоугольных треугольников, для которых хотите выполнить расчет: '))
print(sep)

while i1 <= tr_nums:
    k1_list.append(float(input('Введите длину ПЕРВОГО катета для {}-го треугольника: '.format(i1))))
    i1 += 1
print(sep)

while i2 <= tr_nums:
    k2_list.append(float(input('Введите длину ВТОРОГО катета для {}-го треугольника: '.format(i2))))
    i2 += 1
print(sep)

while i <= tr_nums:
    k1 = k1_list[i-1]
    k2 = k2_list[i-1]
    s = k1 * k2 / 2
    c = (k1**2 + k2**2)**0.5
    print(f'Треугольник {i} с катетами {k1} и {k2} имеет площадь {s} и гипотенузу {c}')
    i += 1
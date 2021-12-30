from lst_for_dict import persons
import collections

i = 0
names = []
ages = []
male_cnt = 0
female_cnt = 0
adult = 0
num_ppl = len(persons)

while i < num_ppl:
    names.append(persons[i]['name'])
    ages.append(persons[i]['age'])
    d = persons[i]
    if 'male' in d.values():
        male_cnt += 1
    if 'female' in d.values():
        female_cnt += 1
    if persons[i]['age'] >= 18:
        adult += 1
    i += 1

unique_names = list(set(names))
unique_ages = list(set(ages))
names_cnt = dict(collections.Counter(names))
mega_names = [k for k in names_cnt.keys() if names_cnt[k] in sorted(names_cnt.values(), reverse=True)[0:3]]
fm_35 = [x['name'] for x in persons if x['gender'] == 'male' and x['age'] > 35 and x['name'].startswith('F')]

print(f'Количество всех людей в списке равно {str(num_ppl)}')
print(f'Мужчин в списке {male_cnt}, а женщин - {female_cnt}')
print(f'Совершеннолетних персон в списке {adult}')
print(f'Перечисление всех имен: {unique_names}')
print(f'Отсортированный список всех возрастов без повторений: {sorted(unique_ages)}')
print(f'Три самых встречающихся имени: {mega_names}')
print(f'Имена мужчин старше 35 лет, имя которых начинается с F: {fm_35}')

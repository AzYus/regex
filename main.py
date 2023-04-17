from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
## Ваш код
#a. Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.

#b. Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
#c.Объединить все дублирующиеся записи о человеке в одну.




## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
#with open("phonebook.csv", "w") as f:
#    datawriter = csv.writer(f, delimiter=',')
#
    ## Вместо contacts_list подставьте свой список:
#    datawriter.writerows(contacts_list)
s = ''
for i in contacts_list:
  s += '\n'
  for l in i:
    s +=(l+',')
p = re.compile('(\,)*')
res = re.sub(p,r'\1', s)
p = re.compile('([А-Я][а-я]+)\s*\,*([А-Я][а-я]+)\s*\,*')
res = re.sub(p,r'\1,\2,', res)
p = re.compile('(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})')
res = re.sub(p,r'+7(\2)\3-\4-\5', res)
p = re.compile('\s*\(*(доб.)\s*(\d+)\)*\s*')
res = re.sub(p,r' \1\2', res)
l = res.split('\n')
l.pop(0)
li =[]
for i in l:
  s=(i.split(','))
  s.remove('')
  li.append(s)
for i in li:
  for s in li:
    try:
      if i[0]==s[0]:
        if i != s:
          print(i,s)
          for q in range(1,10):
            for z in i:
              if z in s:
                i.remove(z)
              else:
                s.append(z)
                i.remove(z)
    except:
      pass
text = ''
for i in li:
  if len(i) == 0:
    li.remove(i)
li.sort()
# for i in li:
#   text += ('\n')
#   for z in i:
#     text +=(z+', ')
# print(text)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',' )
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(li)
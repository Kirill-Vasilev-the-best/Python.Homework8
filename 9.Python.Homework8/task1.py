# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может 
# ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник:\n"
          "2. Найти абонента по фамилии:\n"
          "3. Найти абонента по номеру телефона:\n"
          "4. Добавить абонента в справочник:\n"
          "5. Сохранить справочник в текстовом формате:\n"
          "6. Закончить работу:\n")
    choice = int(input())
    return  choice
def read(file_name):
    data = []
    data1 = ('Фамилия', 'Имя', 'Телефон', 'Описание')
    with open(file_name, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(data1, line.strip().split(',')))
            data.append(record)
    print(data)
read('directory.txt')

def search(data):
    flag = 1
    name = input('имя > ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('имя не указано')

def correct_name(text):
    name = input(f'{text} ')
    while not all(map(str.isalpha,name)):
        print('не корректный ввод')
        name = input(f'{text} ')
    return name.capitalize()
    
name = correct_name('имя')
surname = correct_name('фамилия')

# task1
for i in range(5):
    dictionary = {'АБСТРАКЦИЯ': 'отвлечение от несущевственных деталей ради выделения главного.',
                 "КРИНЖ": "Что-то очень странное или стыдное",
                 "ЛОЛ": "Что-то очень смешное"
                 }
    word = input('какое слово надо?')
    if word in dictionary.keys():
        print(dictionary[word])
    else:
        print('не найдено слова')

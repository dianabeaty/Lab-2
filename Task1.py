from csv import reader

with open('books-en.csv', mode='r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    
    count = sum(1 for row in table if len(row[1]) > 30)

print(f'Количество записей, у которых название книги длиннее 30 символов: {count}')

from csv import reader


output = open('result.txt', 'w')

search = input('Введите автора книги: ')
list_of_books = []

with open('books-en.csv', mode='r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if search.lower() in row[2].lower():
            year = int(row[3])
            if 1997 <= year <= 2000:
                list_of_books.append(row)

if list_of_books:
    print(f'Найдено(а) {len(list_of_books)} книг(а) по автору {search} в период с 1997 по 2000 год:')
    for book in list_of_books:
        print(f"- {book[1]} (Год: {book[3]})")
else:
    print(f'Книги от автора {search} за период с 1997 по 2000 год не найдены.')









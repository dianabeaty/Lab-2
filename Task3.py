import csv
import random


with open('books-en.csv', mode='r', encoding='windows-1251') as file:
    table = csv.reader(file)
    header = next(table)  
    books = list(table)   

sample_books = random.sample(books, 20)


bibliography = []
for book in sample_books:
    first_item = book[0]
    sub_item = first_item.split(';')
    if len(sub_item) >= 3:
        entry = f"<{sub_item[2]}>. <{sub_item[1]}> - <{sub_item[3]}>"
    bibliography.append(entry)
    

with open('bibliography.txt', 'w', encoding='windows-1251') as f:
    for i, entry in enumerate(bibliography, start=1):
        f.write(f"{i}. {entry}\n")

print("Библиографические ссылки сохранены в 'bibliography.txt'")
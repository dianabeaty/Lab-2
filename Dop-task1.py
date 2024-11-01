import csv


unique_publishers = set()

with open('books-en.csv', mode='r', encoding='windows-1251') as csvfile:
    table = csv.reader(csvfile)
    header = next(table)  
    books = list(table)
    for row in books:
        first_item = row[0]
        sub_item = first_item.split(';')
        if len(sub_item) >= 5:
            unique_publishers.add(sub_item[4])

for publisher in sorted(unique_publishers):
    print(publisher)
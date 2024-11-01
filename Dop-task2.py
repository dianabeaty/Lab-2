from csv import DictReader

books = {}

with open('books-en.csv', mode='r', encoding='windows-1251') as csvfile:
    table = DictReader(csvfile, delimiter=';')
    for row in table:
         title = row.get('Book-Title')
         downloads = row.get('Downloads')

         if title and downloads and downloads.isdigit():
            downloads = int(downloads)
            books[title] = downloads

most_popular_books = sorted(books.items(), key=lambda x: x[1], reverse=True)[:20]

print('Top 20 Most Popular Books:')
for title, downloads in most_popular_books:
    print(f"{title}: {downloads} downloads")
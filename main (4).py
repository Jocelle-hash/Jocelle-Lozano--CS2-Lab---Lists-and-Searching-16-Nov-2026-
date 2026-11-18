
books = []
copy = []

for i in range(3):
    book = input("Please enter title of the book: ")
    books.append(book)
    copies = int(input("Enter how many copies: "))
    copy.append(copies)

search = input("enter title of book you want to find: ")

def find(search):
    for i in range(len(books)):
        if books[i] == search:
            return i
    return -1
    
index = find(search)

if index != -1:
    print(books[index], "has", copy[index], "copies")
else:
    print("not in library")
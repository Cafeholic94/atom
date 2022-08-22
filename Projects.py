

# library exchange system
## takes books and allows to check out one book in exchange
book_list = []
while (1==1):
    exit = input(" Type exit to leave the program or any other key to continue to deposit a book: ")
    if exit == "exit":
        break
    book = input("enter the title of the book you wish to deposit: ")
    book_list.append(book)
    answer = input("Do you wish to take out a book: ")
    if answer == "yes":
        see_list = input("Do you want to see the list of available books? ")
        if see_list == "yes":
            print(book_list)
        title = input("Which book do you want to take out?: ")
        if title in book_list:
            print("Okay you've checked out: " + title)
            book_list.remove(title)
        else:
            print("sorry that book is not available")

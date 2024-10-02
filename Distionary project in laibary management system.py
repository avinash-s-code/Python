Library={}
while True:
    print('\n Library Management system')
    print('1.Add Book')
    print('2.View Book')
    print('3.Update Book')
    print('4.Delete Book')
    print('5.Search Book')
    print('6. Count Book')
    print('7.Exist')
    
    choice=input('Enter your choice (1-7)=')

    if choice=='1':
        title =input('Enter book title=')
        if title in Library:
            print('Book already exists!')
        else:
            author=input('Enter author name=')
            year=input('Enter year=')
            Library[title]={ 'author':author, 'year':year}
            print(f' Book "{title}"added to Library.')

    elif choice=='2':
        title=input('Enter book titleto view=')
        if title in Library:
            print(f'Title:{title},Author:{author},Book year:{year}')
        else:
            print('Book not found in Liabrary!')
    elif choice=='3':
        title=input('Enter book title to update=')
        if title in Library:
            author=input('Enter new author name=')
            year=input('Enter new year=')
            Library[title]={'author':author,'year':year}
            print(f'Book"{title}"has been updated!')
        else:
            print('Book not found in the Liabrary!')
    elif choice=='4':
        title=input ('Enter book title to delete=')
        if title in Library:
            del Library[title]
            print(f'Book "{title}" has been deleated successfully!')
        else:
            print('Book not found in library!')

    elif choice=='5':
        search_tearm=input('Enter book title to search=')
        found=False
        for title in Library.items():
            if search_tearm in title:
                print(f'Found-Title:{title},Author:[{author}],Year:{book['year']}')
                found=True
            if not found:
                print('No books found match in that search term!')
    elif choice=='6':
        print(f'Total books in library :{len(Library)}')
    
    elif choice=='7':
        print('Closing the program.......')
        break
    else:
        print('In_valid input')

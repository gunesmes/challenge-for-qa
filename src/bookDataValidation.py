import json, codecs, sys
from operator import itemgetter
import testCase

class BookData():
    def __init__(self, fileName):
        self.data_file = fileName 
        self.fr = open(fileName).read()

        self.filtered_by_keys_number_books = list()
        self.inconsistant_keys_books = list()
        self.filtered_validated_books = list()
        self.filtered_validated_nonempty_books = list()
        self.filtered_validated_nonempty_unique_books = list()
        self.same_record_books = list()
        self.same_id_books = list()

        self.filtered_by_keys_number_authors = list()
        self.inconsistant_keys_authors = list()
        self.filtered_validated_authors = list()
        self.filtered_validated_nonempty_authors = list()
        self.filtered_validated_nonempty_unique_authors = list()
        self.same_record_authors = list()
        self.same_id_authors = list()

        self.invalid_author_books =list()
        self.valid_books = list()

        print "\nTest Case 0: Source should be in JSON format"
        try:
            self.data = json.loads(self.fr)
        except ValueError, e:
            print " Result: FAILED! \n Source data is not in JSON format \n  Reason: %s" %e
            sys.exit()
        print " Result: PASSED! \n Source data is in JSON format"        
    
        
    def check_key_number_book(self):
        books = self.data["books"] 
        failed = []

        for book in books:
            if len(book) != 3:
                failed.append(book)
            else:
                self.filtered_by_keys_number_books.append(book)

        testCase.result(1, failed)      

    
    def validate_keys_book(self):
        # we will remove the books which has invalid keys
        books = self.filtered_by_keys_number_books 
        keys = ["id", "name", "author"]
        failed = []

        for book in books:
            if all(key in book for key in keys):
                self.filtered_validated_books.append(book)
            else:
                failed.append(book)

        testCase.result(2, failed)                
    

    def check_empty_keys_book(self):
        # we will remove the books which has invalid keys
        books = self.filtered_validated_books
        failed = [] 

        for book in books:
            if all(len(book[key]) is not 0 for key in book):
                self.filtered_validated_nonempty_books.append(book)
            else:
                failed.append(book)

        testCase.result(3, failed)
    

    def check_multiple_record_book(self):
        # we will remove 
        books = self.filtered_validated_nonempty_books 
        books = sorted(books, key=itemgetter("id"))
        self.filtered_validated_nonempty_unique_books = books


        i = 0
        while i < len(books)-1:
            id = books[i]["id"]
            name = books[i]["name"]
            author = books[i]["author"]

            if id == books[i+1]["id"]:
                if name == books[i+1]["name"] and author == books[i+1]["author"]:
                    self.same_record_books.append(books[i+1])

                    #  exactly the same record, we should remove others
                    self.filtered_validated_nonempty_unique_books.pop(i+1)
                else:
                    self.same_id_books.append(books[i+1])
                   
                    #  same id but content is different, we should remove all
                    self.filtered_validated_nonempty_unique_books.pop(i) 
                    self.filtered_validated_nonempty_unique_books.pop(i) # i+1 is i now  
            i+=1
        testCase.result(4, self.same_id_books)
        testCase.result(5, self.same_record_books)

        
    def check_key_number_author(self):
        authors = self.data["authors"] 
        failed = []

        for author in authors:
            if len(author) != 2:
                failed.append(author)
            else:
                self.filtered_by_keys_number_authors.append(author)
        
        testCase.result(6, failed)    
    
    def validate_keys_author(self):
        # we will remove the books which has invalid keys
        authors = self.filtered_by_keys_number_authors 
        keys = ["id", "name"]
        failed = []

        for author in authors:
            if all(key in author for key in keys):
                self.filtered_validated_authors.append(author)
            else:
                failed.append(author)
        
        testCase.result(7, failed)   

        
    def check_empty_keys_author(self):
        # we will remove the books which has invalid keys
        authors = self.filtered_validated_authors
        failed = [] 

        for author in authors:
            if all(len(author[key]) is not 0 for key in author):
                self.filtered_validated_nonempty_authors.append(author)
            else:
                failed.append(author)

        testCase.result(8, failed)        
        
    def check_multiple_record_author(self):
        authors = self.filtered_validated_nonempty_authors 
        authors = sorted(authors, key=itemgetter("id"))
        self.filtered_validated_nonempty_unique_authors = authors

        i = 0
        while i < len(authors)-1:
            id = authors[i]["id"]
            name = authors[i]["name"]

            if id == authors[i+1]["id"]:
                if name == authors[i+1]["name"]:
                    self.same_record_authors.append(authors[i+1])

                    #  exactly the same record, we should remove others
                    self.filtered_validated_nonempty_unique_authors.pop(i+1)
                else:
                    self.same_id_authors.append(authors[i+1])

                    #  same id but content is different, we should remove all
                    self.filtered_validated_nonempty_unique_authors.pop(i)
                    self.filtered_validated_nonempty_unique_authors.pop(i+1)
            i+=1

        testCase.result(9, self.same_id_authors)
        testCase.result(10, self.same_record_authors)        
    
        
    def check_author_of_book(self):
        # we will use the books list which has 3 valid keys
        books = self.filtered_validated_nonempty_unique_books
        authors = self.filtered_validated_nonempty_unique_authors

        for i in range(len(books)):
            found = False
            for author in authors:
                if books[i]["author"] == author["id"]:
                    self.valid_books.append(books[i])
                    found = True
                    break
            if found == False:    
                self.invalid_author_books.append(books[i])

        testCase.result(11, self.invalid_author_books)


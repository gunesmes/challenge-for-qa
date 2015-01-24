# -*- coding: utf-8 -*-

import os, sys, getopt
sys.path.append("src")

from bookDataValidation import BookData
import testCase

def validate_book_data(argv):
    try:
        optlist, args = getopt.getopt(sys.argv[1:], "options")
    except getopt.GetoptError, err:
      print err
      sys.exit(2)

    try:
        # give data pull path
        data_file = args[0]

    except IndexError:
        print "Arguments Error! Please run the file with the following format:" 
        print "\n   python run.py 'path/to/data_file'\n"
        sys.exit(2)

    s = BookData(data_file)
    s.check_key_number_book()
    s.validate_keys_book()
    s.check_empty_keys_book()
    s.check_multiple_record_book()
    s.check_key_number_author()
    s.validate_keys_author()
    s.check_empty_keys_author()
    s.check_multiple_record_author()
    s.check_author_of_book()
    testCase.write_data(data_file, s.valid_books, s.filtered_validated_nonempty_unique_authors)

    print "\n" + "- - - - - "*5 + "\n\n Please check 'result' folder for more detail"
    print " * Validated json file is: %s" %(data_file[0: data_file.index('.')] + '_validated.json') 
    print " * Check 'result.txt' for more detail about result\n"

if __name__ == "__main__":
   validate_book_data(sys.argv[1:])

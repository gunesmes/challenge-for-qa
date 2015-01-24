# -*- coding: utf8 -*-
import datetime, json, os

fw = open("result/result.txt", 'w')

def print_new(printStr):
    print printStr        
    fw.write(printStr + "\n")
        
def write_data(name, books, authors):
    os.chdir("result")
    with open(name[0: name.index(".")] + "_validated.json", 'w') as outfile:
        json.dump({"books": books, "authors": authors}, outfile)    


def result(case_number, failed_records):
    print_new("\n\nTest Case %d: %s" %(case_number, testCases[case_number][1]))
    print_new(" Severity: %s" %testCases[case_number][0]) 
    print_new(" Number of Failed Records: %d" %len(failed_records))
    fw.write("Recorded Data: \n %s" %failed_records)



testCases = [
                #[severity, description]
                ['Blocker', 'Source should be in JSON format'],
                ['Major', 'Books should have 3 keys'],
                ['Major', 'Books should have following keys: author, id, name'],
                ['Major', 'Books should have following keys: author, id, name not empty'],
                ['Minor', 'There should be no duplicated book records with same id but different content'],
                ['Minor', 'There should be no duplicated book records with same id and same content'],
                ['Major', 'Author should have 2 keys'],
                ['Major', 'Author should have following keys: id, name'],
                ['Major', 'Author should have following keys: id, name not empty'],
                ['Minor', 'There should be no duplicated author records with same id but different content'],
                ['Minor', 'There should be no duplicated author records with same id and same content'],
                ['Major', 'Books should have a valid author'],
            ]
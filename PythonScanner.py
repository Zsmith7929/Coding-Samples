############################ 123
#                          # 1.23
#  Author: Zacheriah Smith #
#  1/12/16                 #
#  Assignment 1 - CS3120   #
#  Professor Hecker        #
#                          #
############################

import sys
import string
import pprint

class Scanner(object):

    def __init__(self, filepathToScan):
        
        self.filepathToScan = filepathToScan

        self.tokenTable = {"keyword" : {"if":0, "then":0, "else":0, "return":0, "as":0, "with":0, "pass":0,
                                        "for":0, "print":0, "def":0, "in":0, "not":0, "try":0, "except":0,
                                        "while":0, "import":0, "None":0},

                           #python uses dynamic typing but I added some options for fun
                           "identifier" : {"class":0, "bool":0, "char":0, "int":0,
                                           "string":0, "float":0, "long":0},

                           "integer" : {},
                           
                           "real" : {},

                           "special" : {k:0 for k in string.punctuation},

                           "digit" : {k:0 for k in string.digits},

                           "character" : {k:0 for k in string.ascii_letters}}

    def scan(self):

        try:
            #we're only trying because the filepath might be wrong
            with open(self.filepathToScan) as f:
                _raw = f.read()

                #this will sort individual characters
                for x in _raw:
                    for y in self.tokenTable.keys():
                        if x in self.tokenTable[y].keys():
                            self.tokenTable[y][x] += 1
                            
                #this will sort whole phrases delimited by spaces
                for x in _raw.split():

                    item = x.rstrip(string.punctuation)

                    #don't double count single-character words like "I"
                    if len(item) < 2:
                        pass
                    else:
                        
                        for y in self.tokenTable.keys():
                            if item in self.tokenTable[y].keys():
                                self.tokenTable[y][item] += 1

                            #if the 'word' has a digit in it, it's an integer or real  
                        if len([z for z in item if z not in "." and z not in string.digits]) < 1:

                            #check to make sure there decimal, but not at the end of the word as a period
                            if "." in x[:len(x)-1]:
                                #format the real to remove any character not relating to it, ending punctuation, etc
                                real = "".join([z for z in x if z in string.digits or z in string.punctuation])
                                real = real.rstrip(".")
                                if real in self.tokenTable["real"]:
                                    self.tokenTable["real"][real] += 1
                                else:
                                    self.tokenTable["real"][real] = 1
                                    
                            #filter just in case it has punctuation
                            else:
                                if "".join([z for z in x if z in string.digits]) in self.tokenTable["integer"]:
                                    self.tokenTable["integer"]["".join([z for z in x if z in string.digits])] += 1
                                else:
                                    self.tokenTable["integer"]["".join([z for z in x if z in string.digits])] = 1

        except Exception as e:
            print type(e)
            print e.args

    def printTable(self):
        pp = pprint.PrettyPrinter()
        pp.pprint(self.tokenTable)

if __name__ == "__main__":
    
    scanner = Scanner(sys.argv[1])
    scanner.scan()
    scanner.printTable()

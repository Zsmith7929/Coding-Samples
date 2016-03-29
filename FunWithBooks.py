#############################
#                           #
#    Script by: Zac Smith   #
# Email:Smith7929@Yahoo.com #
#                           #
#############################
 
import string as st, random as ra, time as ti

def displayIntro():
    print'''
This tool will take a book file in plain text format and apply the Markov analysis
to determine the relationship between the words in the book.'''

def buildDic(filepath):
    predic = dict()
    book = open(filepath)
    for line in book:
        lineList = line.split()
        newLine = []
        for word in lineList:
            newWord = filter(str.isalnum, word)
            newLine.append(newWord)
        for word in range(len(newLine)):
            if newLine[word] not in predic and word != len(newLine) - 1:
                predic[newLine[word]] = [newLine[word+1]]
            elif newLine[word] in predic and word != len(newLine) - 1:
                predic[newLine[word]].append(newLine[word+1])
            else:
                pass
    return predic

def saySomething(thedic, length=5):
    something = []
    try:
        first = ra.choice(thedic.keys())
    except IndexError:
        print 'The dictionary failed to build. This is probably caused by an improperly formatted text file.'
        print ''
        return getInput()
    
    something.append(first)
    for i in range(length):
        try:
            something.append(ra.choice(thedic[something[i]]))
        except KeyError:
            print 'Unfortunately, the dictionary found no matching "suffix" for the seed word.'
            print 'Likely this is due to a file with too few words to analyze or the use of a non-plain text file.'
            print 'You can try running it again, or select a different file.'
            while True:
                print 'Type "retry" or "exit"'
                choices = raw_input('>> ')
                print ''
                if choices.lower() == 'retry':
                    return saySomething(thedic, length)
                elif choices.lower() == 'exit':
                    return getInput()
                else:
                    print 'Your entry wasn\'t recognized.'
                    print ''
                
    print '='*60
    print 'OUTPUT:'
    print ''
    print ' '.join(something) + '\n'
    print ''
    print '='*60
    print ''
    return getInput()

def getInput():
    while True:
        print 'Please type filename, then a comma, followed by the length of the sentence you want contructed.'
        print '(Example: >>> c:\python27\words.txt, 5), OR type "exit" (without quotations) to exit the script.'
        theinput = raw_input('>> ')
        print ''
        theinput = theinput.strip()
        if theinput.lower() == 'exit':
            return exit()
        else:
            pass            
        try:
            twostring = theinput.split(',')
            filename = twostring[0].strip(st.punctuation + st.whitespace)
            sentLen = twostring[1].strip(st.punctuation + st.whitespace)
        except IndexError:
            print 'Please ensure you have a comma placed between the filename and the phrase length integer.'
            print 'Press "Enter" to continue.'
            raw_input('>> ')
            print ''
            return getInput()
        try:
            outdic = buildDic(filename)
        except IOError:
            print 'Your file "%s" was not found. Please use standard \
format, e.g. (without quotes) "C:\python27\\book.txt"' % (filename)
            print 'Press "Enter" to continue.'
            raw_input('>> ')
            print ''
            return getInput()
        try:
            sentLen = int(sentLen)
            saySomething(outdic, sentLen)
        except ValueError:
            print 'The phrase length you specified was not recognized. Please use a number, e.g. (without quotes) "5"'
            print 'Script will run with a default phrase length of 5. Please press "Enter" to continue.'
            raw_input('>> ')
            print ''
            saySomething(outdic)





displayIntro()
getInput()





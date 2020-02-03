

'''

len() - length of string or list

File stuff:

afile = open("name of that file",'w')
afile.write('line 1 \n line 2')
afile.close()

prefixes: 
'r' - read
'w' - write
and others

anotherfile = open("name of that file",'r')
content = anotherfile.read()    or can do .readline() - > makes each line an entry in a list
anotherfile.close()
print(content)


string processing:

split() - splits the string into seperate words while forming a list

x = "word1 word2 word3"
print(x.split())


strip() - removes whitespaces/lines/tabs aka compacts from beggining and end

x = "\n some \n stupid \n text \n here \n"
strippedstring = x.strip()
print(strippedstring)


'''

#LAB 5 - minor 3

'''
infile1 = open("wc.txt", 'w')
infile1.write("This will enter some text\ninto the file I am testing.")
infile1.close()

infile2 = open("wc2.txt", 'w')
infile2.write("Abilities forfeited situation extremely my to he resembled.\nOld had conviction discretion understood put principles you.\nMatch means keeps round one her quick.\nShe forming two comfort invited. Yet she income effect edward. Entire desire way design few.\nMrs sentiments led solicitude estimating friendship fat. Meant those event is weeks state it to or. Boy but has folly charm there its. Its fact ten spot drew.")
infile2.close()

infile3 = open("wc3.txt", 'w')
infile3.write("Sussex result matter any end see. It speedily me addition weddings vicinity in pleasure. Happiness commanded an conveying breakfast in.\nRegard her say warmly elinor. Him these are visit front end for seven walls.\nMoney eat scale now ask law learn. Side its they just any upon see last. He prepared no shutters perceive do greatest. Ye at unpleasant solicitude in companions interested.")
infile3.close()

infile4 = open("wc4.txt", 'w')
infile4.write("9")
infile4.close()
'''

def minor3(a,b,c,d): 
    
    filelist = [a,b,c,d]


    lineCount = 0     
    wordCount = 0     
    charCount = 0

    for filenum in range(len(filelist)):
        currentfile = open(filelist[filenum],"r")

        content = currentfile.read()

        #lines = []

        lines = len((open(filelist[filenum],"r").readlines()))

        char = len(content) - (lines - 1)

        words = len(open(filelist[filenum],"r").read().split()) 

        print('File name:' + filelist[filenum])

        print('lines:',lines)

        print('words:',words)

        print('char:',char)

        currentfile.close()

        #print(content + "\n")

    lineCount = lines
    wordCount = words
    charCount = char
    
    return lineCount, wordCount, charCount

result = minor3("wc.txt","wc2.txt","wc3.txt","wc4.txt")

'''
Design questions:

1. What is the best way to compute the number of lines, words, and characters 
in a file: by reading the file once, or by reading the file three times?

either one, we could use seek(0,0) to move cursor to the beggining

2. When printing to the screen, the syntax `print("x=", x, "\n")` and
`print("x="+str(x)+"\n")` are both valid. Is this true when using `file.write()`?

??? is it?


3. Is it better if most of the test cases for your program 
are files containing many lines of text? Explain your answer

no because we are testing edge cases or different types if symbol

4. What is the difference between `read()` and `readlines()`?

read() is just a big string, while readlines() is a list of strings depedning on their line


'''



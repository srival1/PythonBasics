with open("testdata.txt", 'r') as readfile: # another way to open the file and this do not need an explicit close statement
    readlist = readfile.readlines()
    print(readlist)
    with open("testdata.txt", 'w') as writefile:
        for writeline in reversed(readlist):
            #if not writeline.endswith("\n"):
            #    writeline = writeline + "\n"
            writefile.write(writeline)

readfile = open("testdata.txt", 'r')
readfile.seek(0)
print(readfile.readlines())
readfile.close()
print("####################################################################################")
readerlist = ""
writerline = ""
with open("testdata.txt", 'r') as readerfile:
    with open("testdata1.txt", 'w') as writerfile:
        readerlist = readerfile.readlines()
        for writerline in reversed(readerlist):
            #if not writeline.endswith("\n"):
            #    writeline = writeline + "\n"
            writerfile.write(writerline)


with open("testdata1.txt", 'r') as readingfile:
    readingfile.seek(0)
    print(readingfile.readlines())
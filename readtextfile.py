file = open('testdata.txt')

print(file.read(3))

file.seek(0)
print(file.read())
print("####################################################################################")
file.seek(0)
print(file.readline())
print(file.readline())
print("####################################################################################")
file.seek(0)
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
print("####################################################################################")
file.seek(0)
lineslist = file.readlines()
for line in lineslist:
    print(line)
    if line.__contains__("Cat"):
        print("Found the Cat")
file.close()

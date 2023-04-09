str1 = 'RahulShettyAcademy'
str2 = ".com"
int1 = 1
str3 = 'Shetty'
print(str1[1])
print(str1[0:5])
print(str1[5:11])
print(str1[11:18])

str4 = "12/31/2000"
print(str4[0:2])
print(str4[3:5])
print(str4[6:])

print(str1+str2)    #concatenate str with str
print(str1+" is # {} online tutor".format(int1)) #concatenate int with str

print(str3 in str1) #substring check

str4 = str1 + str2
splitlist = str4.split(".")
print(splitlist)
print(splitlist[0])
print(splitlist[1])

str5 = " Karth i Keyansh "
print(str5.strip())
print(str5.lstrip())
print(str5.rstrip())
print(str5.startswith(' '))

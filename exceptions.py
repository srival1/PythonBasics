itemsincart = 0

if itemsincart != 2:
    #raise Exception("items count do not match")
    pass

#assert(itemsincart != 2, print("True"))
assert(itemsincart == 0)

try:
    assert(itemsincart == 2)
except Exception as e:
    print(e)

try:
    with open("filelog.txt",'r') as reader:
        reader.read()
except Exception as error:
    print(error)

try:
    with open("filelog.txt",'r') as reader:
        reader.read()
except:
    print("FileLog text file Not Found")
finally:
    print("I am the Finally Block Executed With Exception")

try:
    with open("testdata.txt",'r') as reader:
        reader.read()
except:
    print("FileLog text file Not Found")
finally:
    print("I am the Finally Block Executed Even Without Exception")
    #we can do cleanup records or other tear down activities here

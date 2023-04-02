print("\n############################# IF ELIF ELSE #############################################")
greeting = "Good Morning"

if greeting == 'Morning':
    print("True")
elif greeting == "Good Morning":
    print('Super True')
else:
    print("False")

print("\n############################# FOR LOOP #############################################")
# For loops are used to run the loop for a range of values
List_Object = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in List_Object:
    print(i)

for i in List_Object:
    if i % 2 == 0:
        print("{} is an Even Number".format(i))
    else:
        print("{} is an Odd Number".format(i))

for j in range(0,4): # range(i,j) --> i thru j-1
    print(j)

summ = 0
for k in range(0, 10):
    summ += k
    print(k, summ)

minus = 0
for l in range(0, 10, 2):
    minus -= l
    print(l, minus)

for m in range(5): # starts from 0 if min value is not specified
    print(m)

print("\n############################### WHILE LOOP ##############################################")
# While loops are used to run the loop until a specific condition is met

val = 1
while val < 5:
    print(val)
    val = val + 1

val1 = 5
while val1 > 0:
    if val1 != 1:
        print(val1)
    elif val == 2:
        continue  # will skip that one iteration and moves to next iteration
    else:
        break
    val1 = val1 - 1

print("\n############################### DO WHILE LOOP ##############################################")
counter = 0
while True:
    print(counter)
    counter += 2
    if counter == 10:
        break


secret_word = "python"
count = 1

while True:
    word = input("Enter the secret word: ").lower()
    count = count + 1
    if word == secret_word:
        break
    if word != secret_word and count > 3:
        break

#Standard Encodings https://docs.python.org/2.4/lib/standard-encodings.html
# try utf8 or latin_1

# 1 dir up
inputfile = "../user_names.txt"

myfile = open(inputfile, mode='r', encoding='ascii')

#print(myfile.read())

for num, line in enumerate(myfile, 1):
    if "A" in line:
        print("Line Nr:  " + str(num) + " : " + line.strip())



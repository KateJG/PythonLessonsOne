
#Standard Encodings https://docs.python.org/2.4/lib/standard-encodings.html
# try utf8 or latin_1

# 1 dir up
inputfile = "C:/MyPython/FirstProjects/list_of_passwords.txt"
outputfile = "./my_passwords.txt"

myinfile = open(inputfile, mode='r', encoding='latin_1')
#myoutfile = open(outputfile, mode='w',encoding= 'latin_1')
#append to the same file
myoutfile = open(outputfile, mode='a',encoding= 'latin_1')
password_tolookfor = "petya"

#print(myinfile.read())

for num, line in enumerate(myinfile, 1):
    if password_tolookfor in line:
        print("Line Nr:  " + str(num) + " : " + line.strip())
        myoutfile.write("Found password: " + line)

myinfile.close()
myoutfile.close()



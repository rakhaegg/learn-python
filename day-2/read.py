

file = open("file.txt" , "r")
line = file.readline()

while line :
    print(line[0] + str(len(line) - line.count("\n")))

    line = file.readline()


file.close()
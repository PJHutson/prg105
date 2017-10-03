# open a file: filevar.open("<filename>", "<mode>"), mode = r, w, a

infile = open("names.txt")

# use a while loop to read the file
name = infile.readline()        # get the first line
LinesRead = 0                   # count the names

while name != "":           # test for an empty string
    print(name, end="")     # all on one line
    name = infile.readline()        # get next line
    LinesRead = LinesRead + 1

print(name)
print("The file has", LinesRead, "names")           # Total names read

infile.close()

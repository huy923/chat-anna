import glob, os
os.chdir("./data")
allfile = []
for file in glob.glob("*.txt"):
    allfile.append(file)
    print(file)
print([x for x in allfile])
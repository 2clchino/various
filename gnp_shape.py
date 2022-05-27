import glob
files = glob.glob("./*.dat")
for file in files:
    with open(file) as fr:
        lines = fr.readlines()
        terms = []
        for line in lines:
            if(line[0] != "#"):
                print(line)
                term = line.split(" ")
                print(term)
                terms.append(term[len(term) - 2])
        with open(file[:2]+"key_"+file[2:], mode="w") as fw:
            fw.write("\n".join(terms))
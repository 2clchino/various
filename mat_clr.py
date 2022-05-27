import re
import glob
files = glob.glob("./Materials/*.mat")
for file in files:
    with open(file) as f:
        base_color_index = 0
        shade_color_index = 0
        em_color_index = 0
        format = f.readlines()
        for i in range(0, len(format)):
            if ("- _BaseColor:" in format[i]):
                print(i)
                base_color_index = i
            elif ("- _ColorDim:" in format[i]):
                print(i)
                shade_color_index = i
            elif ("- _EmissionColor:" in format[i]):
                print(i)
                em_color_index = i
        for i in range(len(format)):
            if "_Color:" in format[i]:
                color_text = re.findall("(?<=\{).+?(?=\})", format[i])[0]
                cs =color_text.split(',')
                cd = []
                ce = []
                for i in range(0, len(cs)-1):
                    cd.append(round(float(cs[i].replace(' ', '')[2:])*0.75, 5))
                    ce.append(round(float(cs[i].replace(' ', '')[2:])*1.2, 5))
                if (base_color_index != 0):
                    format[base_color_index] = "    - _BaseColor: {"+color_text+"}" + "\n"
                else:
                    format.append("    - _BaseColor: {"+color_text+"}" + "\n")
                if (shade_color_index != 0):
                    format[shade_color_index] = "    - _ColorDim: {r: "+str(cd[0])+", g:"+str(cd[1])+", b:"+str(cd[2])+","+cs[3]+"}" + "\n"
                else:
                    format.append("    - _ColorDim: {r: "+str(cd[0])+", g:"+str(cd[1])+", b:"+str(cd[2])+","+cs[3]+"}" + "\n")
                #s[em_color_index] = "- _EmissionColor: {r: "+str(ce[0])+", g:"+str(ce[1])+", b:"+str(ce[2])+","+cs[3]+"}"
                with open(file, mode="w") as f:
                    f.write("".join(format))
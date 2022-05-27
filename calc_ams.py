import statistics
import math
f = open('0501_go_prodserver.txt', 'r', encoding='UTF-8')
datalist = f.readlines()
time = []
for i in range(len(datalist)):
    time.append(float(datalist[i][7:].rstrip('\n')))
    print("times" + str(time[i]*float(1000)) + "ms")
print("ave: " + str(statistics.mean(time)))
print("med: " + str(statistics.median(time)))
print("std: " + str(statistics.pstdev(time)))
f.close()
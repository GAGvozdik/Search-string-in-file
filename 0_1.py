import csv
import pandas
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
# положение графиков
ax1 = fig.add_subplot(111)

# открываю файл с точками карты
file = open("C:\\Users\\fenik\\Desktop\\python\\тесак\\06_09+трек_виталик.txt")

Result = open('06_09+трек_виталик_result.xls', 'w')  # записываем результаты в файл
Result.write("lat\tlot\tele\tname\t\n")
# массивы куда будут забиваться широты и долготы точек карты
map_longitude = []
map_latitude = []
name = []
ele = []

# заполняю массивы с точками данными из файла, разделяя широты и долготы по точке
for line in file:
    if ' lat=' in line:
        mm = line.strip().split('"')
        map_latitude.append(mm[1])
        map_longitude.append(mm[3])

        Result.write(map_latitude[-1] + '\t')
        Result.write(map_longitude[-1] + '\t')

    if '<ele>' in line:
        nn = line.strip().split('<')
        nnn = nn[1].strip().split('>')
        ele.append(nnn[1])

        Result.write(ele[-1] + '\t')

    if '<name>' in line:
        kk = line.strip().split('<')
        kkk = kk[1].strip().split('>')
        name.append(kkk[-1])

        Result.write(name[-1] + '\n')

Result.close()


import csv
import os
import re

def file_name(file_dir,formula): #查找文件名，并更改为txt格式。

    L=[]

    for dirpath, dirnames, filenames in os.walk(file_dir):

        for file in filenames :

            flag = 0

            portion = os.path.splitext(file)

            if(portion[0] == 'Status'):

                continue

            if portion[1] == '.outmol':

                path0 = os.path.join(dirpath,file)

                newname = path0.replace('.outmol','.txt')

                os.rename(path0, newname)

                L.append(newname)

                formula.append(portion[0])

                flag = 1

            if (portion[1] == '.txt') and (flag == 0):

                path0 = os.path.join(dirpath, file)

                L.append(path0)

                formula.append(portion[0])

    return L

def search(name,homo,lumo):    #寻找homo，lumo，并计算band gap

    flag = 0

    with open(name, "r") as f: #打开转完成的

        get = 'Energy of Highest Occupied Molecular Orbital:'

        for line in f.readlines():

            line = line.strip('\n')  # 去掉列表中每一个元素的换行符

            if (flag == 1):

                lumo = re.findall(r"\d+\.?\d*", line)

                flag = 0

            if (get in line):

                homo = re.findall(r"\d+\.?\d*", line)  # 在字符串中找到正则表达式所匹配的所有数字，a是一个list

                flag = 1

        b = [homo[0],lumo[0],0]

        b[0] = float(b[0])

        b[0] = 0 - b[0]

        b[1] = float(b[1])

        b[1] = 0 - b[1]

        b[2] = round(b[1] - b[0],5)

        return b

        # temp = str(line)

#a = os.listdir('E:/钙钛矿项目/Cs1Rb3GeX6')

formula = []

a = file_name('all',formula)

homo = []

lumo = []

temp = []

ans = []

path = 'output.csv'

with open(path,'w',newline="") as f:

    csv_write = csv.writer(f)

    csv_write.writerow(['fomula','homo','lumo','band gap'])

    for i in range(len(a)):

        temp = formula[i].split() + search(a[i], homo, lumo)

        csv_write.writerow(temp)


#search(homo,lumo)






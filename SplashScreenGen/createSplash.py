#! /usr/bin/python

splashDesign = []
pxls = []

with open("splashDesign.txt", "r") as splashfile:
    splashDesign = splashfile.readlines()


for i in range(len(splashDesign)):
    ln = list(splashDesign[i])
    for n in range(len(ln)):
        if ln[n] == '/n' or ln[n] == '0':
            continue
        pxl = [i+1, n+1]
        pxls.append(pxl)

print(pxls)


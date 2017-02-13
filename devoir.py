#coding: utf-8 

for annee in range(1930,2018) :
    for numero in range (0,1000) :
        print(str(annee)[2:] + format(numero,"03d"));




#-------Bibliothèques---------------------

import re
import os
import csv
from collections import Counter
import matplotlib.pyplot as plt



#------Traitement fichier txt---------------------------

file = open('sae15.txt', 'r')

lines = "DATE, IP SOURCE, IP DESTINATION, FLAG, SEQUENCE, ACK, WIN, OPTION, LENGTH \n"
for line in file:
    m = re.findall("..:..:..", line)
    for x in m:
        lines +=  line

lines = lines.replace(">", "")
lines = lines.replace("Flags", "")
lines = lines.replace("seq", "")
lines = lines.replace("ack", "")
lines = lines.replace("win", "")
lines = lines.replace("option", "")
lines = lines.replace("length", "")
lines = lines.replace("IP", "")

lines = lines.replace(",", " ")
lines = lines.replace("  ", ",")
lines = lines.replace(" ", "")


myText = open(r'lines.csv', 'w')
myText.write(lines)
myText.close()

#---------Récupération adresses IP--------------------

file = open('lines.csv')
reader = csv.reader(file)

ip_source = []
ip_destination = []

for line in reader:
    source = line[1]
    destination = line[2]
    source = line[1].rsplit(".",1)[0]
    destination = line[2].rsplit(".",1)[0]
    
    ip_source.append(source)
    ip_destination.append(destination)


#----------------Affichage occurences adresses IP----------


src = Counter(ip_source)
tri_src = {val[0] : val[1] for val in sorted(src.items(), key = lambda x: (-x[1], x[0]))}

print(list(tri_src.items())[:5])

print("\n")


dst = Counter(ip_destination)


tri_dest = {val[0] : val[1] for val in sorted(dst.items(), key = lambda x: (-x[1], x[0]))}
print(list(tri_dest.items())[:5])









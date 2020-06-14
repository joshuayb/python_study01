import csv  
from random import *

ref = [['P' + str(i), 'H' + str(randint(1,10)), 'W' + str(round(abs(10 * normalvariate(0,1))))] for i in range(1,20)]

fields = ['id', 'geo']  
rows = [['P' + str(i+1), ref[i][1] if random() > 0.2 else ref[i][2] if random() > 0.2 else 'S' + str(round(abs(20 * normalvariate(0,1))))] for i in range(0,19)]
print (rows)

rows2 = [['P' + str(i+1), rows[i][1] if random() > 0.4 else ref[i][1] if random() > 0.2 else ref[i][2] if random() > 0.2 else 'S' + str(round(abs(20 * normalvariate(0,1))))] for i in range(0,19)]
print (rows2)

filename = "mycsv1.csv" 
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)   
    csvwriter.writerows(rows) 

filename = "mycsv2.csv" 
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)   
    csvwriter.writerows(rows2) 

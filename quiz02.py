
name ="https://www.youtube.com/watch?v=j_rca1hY9I8"
cut1 = name.index(".")
cut2 = name.index(".", cut1 + 1)
print (cut1, cut2)
pw0 = name[cut1+1:cut2]
print (pw0)
pw1 = pw0[:3]+str(len(pw0))+str(name.count("u"))+"!"
print (pw1)
print (pw0[:3]+str(name.count("u"))+"!")

from random import *
rep = range(1, 21)
rep =list(rep)
shuffle(rep)
winners = sample (rep, 4)
print (rep)

print ("Winners")
print ("1st prize : {0}" . format(winners[0]))
print ("2nd prize : {0}" . format(winners[1:]))







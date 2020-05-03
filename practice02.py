subway =["Joshua", "TTZhao"]
subway.append ("Evelyn")
subway.insert (3,"nini")
print (subway.pop())
print (subway)
num_list = [5,4,3,1,2,9]
num_list.reverse()
num_list.extend(subway)
print (num_list)
cabinet = {3:"Joshua", 100:"TT"}
print (cabinet.get(5, "Available"))
print (3 in cabinet)
cabinet[3] ="Evelyn"
print (cabinet.keys())
print (cabinet.values())
print (cabinet.items())

java = {"tom","sam","dave"}
python = {"josh", "eya", "dave"}
java.add("enem")
print (java & python)
print (java | python)
print (java - python)
print (python - java)
java = list(java)
print (java, type(java))
java = tuple(java)
print (java, type(java))

weather = input("how's the weather? ")
if weather == "rainy" or weather == "snowy":
    print ("take an umbrella")
elif weather =="cold":
    print ("take a coat")
else:
    print ("take it easy")

temp = int(input("How's the temperature? "))
if 30 <= temp:
    print ("hot")
elif 10 <= temp and temp < 30:
    print ("fine")
else:
    print ("cold")
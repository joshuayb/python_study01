#for waiting_no in [0,1,2,3,4]:
 #   print ("대기번호 : {0}". format(waiting_no))

for waiting_no in range(1,6):
    print ("대기번호 : {0}". format(waiting_no))

starbuck = ["ironman", "thor", "ima groot"]
for customer in starbuck:
    print ("{0}, your coffee is ready" .format(customer))

# while
customer = "Thor"
index = 5
while index >= 1:
    print ("{0}, your coffee is ready. you have {1} chances." .format(customer, index))
    index -= 1
    if index == 0:
        print("Your coffee is in the garbage bin")

## infinite loop
#customer = "Thor"
#index = 1
#while True:
 #   print("{0}, your coffee is ready. call {1} times".format(customer, index))
  #  index += 1

## while input

#customer ="Joshua"
#person = "Unknown"

#while person != customer:
#   print("{0}, your coffee is ready." .format(customer))
#   person = input("what is your name?")
#print ("here's your coffee")

absent = [2,4,5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("we finish class. {0}, come to my room." .format(student))
        break
    print("{0}, please read the book." .format(student))

students = ["iron man", "thor", "i am groot"]
students = [len(i) for i in students]
students = [i+100 for i in students]
print (students)

students = ["iron man", "thor", "i am groot"]
students = [i.upper() for i in students]
print (students)




# Make a Program that asks for the 4 bimonthly grades and shows the average.

list = []

for i in range(4):
    grades = int(input("enter your school grade:"))
    list.append(grades)
    
count = 0

for x in list:
   count += x
    
print("your school average is",count/4)


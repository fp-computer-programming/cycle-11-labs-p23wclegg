#Lab_11-2

Grades= {"Mid Year Project Presentation": 93, "Mid Year Project Proposal": 9,
 "Mid Year Project Code": 94, "Mid Year Proejct Reflection": 93}

#Dictionary of my grades
print(Grades.values())
#Printing only the grade value 

for key in Grades:
    print(key)
    
for key in Grades:
    if Grades[key]>70:
        print(Grades.key())

for k in Grades: # Print all below 50
    if Grades[key] < 50:
        print(Grades.key())
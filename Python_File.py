# Tuples data type
S=("Abdi","Sam","Ali","Grace")
M=(40,70,80,90)
print("Student name is",S[0],"Student marks is",M[0],
      "\nStudent name is",S[1],"Student marks is",M[1],
      "\nStudent name is",S[2],"Student marks is",M[2],
      "\nStudent name is",S[3],"Student marks is",M[3])
#range data type
r1=range(8)
r2=range(2,10)
r3=range(0,5,2)
print(r1)
print(list(r1))
print(list(r2))
print(list(r3))
for i in range(2,10):
    print(i)
    #Mapping data type - Dictionery(dict)
Students={"Name":"Ali","Age":20,"course name":["Statistics","Medicine","Biochemistry"]}    
print(Students["Name"])
print(Students["Age"])
print("course name is",Students["course name"][0])

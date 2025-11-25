#Set data types
Courses={"Biochemistry","Medicine","Law","Social Science","Education"}
print(Courses)
#Adding set
Courses.add("Statistics")
print(Courses)
#Remove set
Courses.remove("Statistics")
print(Courses)
#Adding and Discarding a set
Courses.add("Statistics")
print(Courses)
Courses.discard("Statistics")
print(Courses)
Courses.discard("Statistics")
print(Courses)
#Set Operation
a={1,2,3,4}
b={3,4,5,6}
print ("Union",(a|b)) #Union set
print("Intersection",(a&b)) # Intersection
print("Difference",(a-b)) # Difference
print("Difference",(b-a)) # Difference
print("Symmetric difference",(a^b)) # Symmetric Difference
print("Symmetric difference",(b^a)) # Symmetric Difference

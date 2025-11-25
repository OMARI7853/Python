#Dictioneries
Students={"name":"Aisha","age":17,"subjects":["math","english","biology"]}
#copy Students["subjects"]
newlist=Students["subjects"]
len(newlist)
print("Number of subjects",len(newlist))
print("Students")
Students["grade"]="A"  #Add a key
print("Added a key",Students)
Students["age"]=18 #change value
print("Change the value age",Students)
print("Updated dictionery",Students)
Students.pop("age")  #Remove value
print("Remove the value age",Students)
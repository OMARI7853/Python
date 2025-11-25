# Grading of a marks
score = int(input("enter grade:"))
if (score>0):
    print ("These is a grading system")
    if (score>=80):
        print("grade A")
    elif (score>=70):
        print("grade B")
    elif (score>=60):
        print("grade C")
    elif (score>=50):
        print("grade D")
    elif (score>=40):
        print("grade E")
    else:
        print("grade Y")
else:
    print("you entered a negative score")


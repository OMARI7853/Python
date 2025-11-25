#SETS (Removing Duplicates & Set Operations)
raw_registrations = [
    "Amina", "Brian", "Cynthia", "Amina", "David",
    "Brian", "Esther", "Cynthia", "Fatma", "George", "Fatma"
]
#Convert the list into a set to remove duplicates
unique_participants = set(raw_registrations)
print(unique_participants)
#The number of unique participants
print("Unique participants",len(unique_participants))
#The cleaned list of participants
print("Cleaned participant list", unique_participants)
#A second list represents students who actually attended the event
attended = {"Amina", "David", "George", "Yvonne"}
#Who registered but didn’t attend
did_not_attend = unique_participants - attended
print(did_not_attend)
#Who attended but didn’t register
walk_ins = attended - unique_participants
print(walk_ins)
#Who registered and attended
perfect_matches = unique_participants & attended
print(perfect_matches)

# Meal Combinations in a School Cafeteria
combo1 = {"rice", "beans", "juice"}
combo2 = {"chapati", "beans", "juice"}
combo3 = {"rice", "beans", "juice"}  # duplicate
#Store all combos in a list.
meal_list=[combo1,combo2,combo3]
print(meal_list)
#Convert each combo into a frozenset, then add them into a set to remove duplicate combinations.
unique_meals = set()
for combo in  meal_list: unique_meals.add(frozenset(combo))
print(unique_meals)
#The number of unique meal combos
print("number of unique meal combos",len(unique_meals))
#The unique combos themselves
print("number of unique meal combos",len(unique_meals))
# Access Control for a Computer Lab
#User inputs(True/False)
has_id = input("Do you have a valid school ID (True/False)? ") == "True"
paid_fee = input("Have you paid the ICT fee (True/False)? ") == "True"
is_scholar = input("Are you a scholarship student (True/False)? ") == "True"
# Bonus rule: scholarship student without ID
if is_scholar and not has_id:
    print("Warning: Scholarship student must replace missing ID.")

# Access rule:
# Must have ID AND (paid_fee OR is_scholar)
if has_id and (paid_fee or is_scholar):
    print("Access Granted")
else:
    print("Access Denied")


#Input from the user
u_name=input("What is your name")
print(u_name)
u_admission_number=int(input("What is your admission number"))
print(u_admission_number)
print(type(u_admission_number))
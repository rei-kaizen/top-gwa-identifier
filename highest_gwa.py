#open and read the contents of the students file
file = open("students.txt", "r")
contents = file.readlines()

#convert all the contents to a list of dictionaries
#initialize an empty list for marklist1
marklist1 = []
#loop through the contents
for line in contents:
    #split the name and gwa to each other
    name, gwa = line.split(":")
    #and remove the whitespaces characters and add it to the list
    marklist1.append({"name" : name.strip(), "gwa": float(gwa.strip())}) 

#find the top student with the highest gwa
#intialize student order to 0 to keep track
student_order = 0
#store the current top student
top_student = marklist1[student_order]
#store the highest gwa 
highest_gwa = marklist1[student_order]["gwa"]

#iterate until the higher gwa is found for each of the remaining students in the marklist
while student_order < len(marklist1) - 1:
    student_order +=1
    if marklist1[student_order]["gwa"] < highest_gwa:
        highest_gwa = marklist1[student_order]["gwa"]
        top_student = marklist1[student_order]
        
#print the output
print(f"Student with the highest GWA is {top_student['name']}, {top_student['gwa']}")

file.close()
#to have a list of names with gwa for students file

import random

#create a function to generate random gwa
def gwa_generator():
    #generate a gwa between 1.0 and 5.0
    random_gwa = random.uniform(1.0, 5.0)
    #return the gwa to 2 decimal places
    return round(random_gwa, 2)

#have a list of student names
names = ["Choi Seungcheol", "Yoon Jeonghan", "Hong Jisoo", "Wen Junhui", "Kwon Soonyoung",
         "Lee Wonwoo", "Lee Jihoon", "Lee Seokmin", "Kim Mingyu", "Xu Minghao",
         "Boo Seungkwan", "Choi Hansol", "Lee Chan", "Tumas Kong", "Ading Khel",
         "Canny Vincent", "Oniz Nano", "Harlong Short", "Qiqi Batas", "Lucky White"]

#initialize an empty list to store the student's record
marklist = []
#loop through the names of the students
for name in names:
    #call the gwa generator function to get the random gwa
    gwa = gwa_generator()
    #append the dictionary contains the student's name and gwa as keys to the marklist
    marklist.append({"name": name, "gwa" : gwa})

#open a file for writing the student record     
file = open("students.txt", "w")
#looping through the marklist
for student in marklist:
    #write the name and gwa in a separate line
    file.write(f"{student['name']}: {student['gwa']}\n")

#close the file
file.close()

    
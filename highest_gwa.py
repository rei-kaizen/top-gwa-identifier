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

print(marklist1)

#find the top student with the highest gwa
#print the output

file.close()
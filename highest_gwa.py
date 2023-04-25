#open and read the contents of the students file
file = open("students.txt", "r")
contents = file.readlines()

print(contents)

#convert all the contents to a list of dictionaries
#find the top student with the highest gwa
#print the output
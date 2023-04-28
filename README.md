# Top GWA Identifier
This program generates a random GWAs (General Weighted Average) for each student in the given list of names, saves it in a file, and reads the file to identify the student with the highest GWA.

## The program consists of two parts:

### GWA Generator
1. The first part generates a random GWA for each student in the given list of names.<br>
2. A function called `gwa_generator()` is used to generate a random GWA between 1.0 and 5.0, and the result is rounded off to 2 decimal places.<br>
3. A list of student names is created and a dictionary with each student's name and corresponding random GWA is appended to the marklist.<br>
4. Finally, the program writes the student name and GWA to a file.<br>

### Finding the student with the highest GWA
1. The second part of the program opens and reads the contents of the students' file. <br>
2. The contents of the file are converted to a list of dictionaries with the student's name and GWA as keys.<br>
3. The program then finds the student with the highest GWA in the list using a `while` loop and conditional statements.<br>
4. Finally, the program prints out the name and GWA of the student with the highest GWA.<br>

## 📄 Documentation 
<details><summary><h3> 🤔 Usage </h3></summary>

-----

1. Run the program in a Python environment. <br>
2. Create a new file and copy the code and paste it into your file.
3. Save the file with a descriptive name and a .py extension (e.g., student_gwa.py).
4. Run the program by clicking on the Run button or by typing "python student_gwa.py" in the terminal.

or
1. Fork this repository 
2. Once the repository has been forked, you can clone the repository to your local machine using the `git clone` command followed by the repository URL.
3. Once the repository is cloned, navigate to the directory of the cloned repository using the `cd` command.
4. Now you can work with the files in the cloned repository.
5. If you want to keep your fork in sync with this repository, you can use the `git fetch` and `git merge` commands to pull in changes and merge them into your local copy.

**Reminders:**
> The program generates random GWAs for each student in the given list of names, so the results will be different each time you run the program.
 The program creates a new file with the student name and GWA. If you run the program multiple times, the previous file will be overwritten.
 The program requires two parts to work, and it's essential to run both parts in the correct order.

</details>

<details><summary><h3> 🔰 Additional information </h3></summary>

-----

**Program 1: Random GWA Generator**
<br>
-The first program generates a list of students with their respective random GWA using the `gwa_generator` function and the list of student names.<br>
-It then saves the list of student record in a file named "students.txt" using the `open()` method and the `write()` method.
<br>
**Program 2: Student with highest GWA**
<br>
The second program reads the student record in the "students.txt" file using the `open()` method and the `readlines()` method.
It then converts the contents of the file to a list of dictionaries, where each dictionary represents a student record using a `for` loop and the `split()` method.
It then uses a `while` loop to find the student with the highest GWA.
The output is displayed in the console using the `print()` method.

</details>

<details><summary><h3> 💡 Purpose </h3></summary>

-----

This program can be a useful tool for automatically displaying the top student with his or her respective GWA among a list of students.

</details>


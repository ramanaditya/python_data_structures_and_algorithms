#Uses python3
#Question is commented below

Courses = []
Students = {}
Grades = {}
while(True):
    get_input = input() #Getting the input
    if get_input == 'Courses':
        value = 1
    elif get_input == 'Students':
        value = 2
    elif get_input == 'Grades':
        value = 3
    elif get_input == 'EndOfInput':
        break
    else:
        get_info = get_input.split('~') #Splitting the input and binding in List
        if value == 1:
            Courses.append(get_info)
        elif value == 2:
            Students[get_info[0]] = get_info[1] #Storing the Roll Number and name as they will be used later
            Grades[get_info[0]] = [] #Creating the key for the dictionary and value as list now its empty
        elif value == 3:
            Grades[get_info[-2]].append(get_info[-1]) #Storing the grades corresponding to the roll number in the list created above

point_table = {'A' : 10 , 'AB' : 9 , 'B' : 8 , 'BC' : 7 , 'C' : 6 , 'CD' : 5 , 'D' : 4}

for grade in sorted(Grades):
    point_list = [point_table[x] for x in Grades[grade]] #Making a list of points corresponding to the grades
    n = len(point_list) or 1 #If list is empty it assigns the value of n as 1
    grade_points = str(round(sum(point_list)/n,2)) if point_list else '0'
    marksheet = [grade,Students[grade],grade_points]
    print('~'.join(marksheet)) #Required output



'''
For this assignment, you have to write a complete Python program. Paste your code in the window below.
You may define additional auxiliary functions as needed.
There are some public test cases and some (hidden) private test cases.
"Compile and run" will evaluate your submission against the public test cases.
"Submit" will evaluate your submission against the hidden private test cases and report a score on 100. There are 6 private testcases in all.
Ignore warnings about "Presentation errors".
The academic office at the Hogwarts School of Witchcraft and Wizardry has compiled data about students' grades. The data is provided as text from standard input in three parts: information about courses, information about students and information about grades. Each part has a specific line format, described below..

Information about courses
Line format: Course Code~Course Name~Semester~Year~Instructor
Information about students
Line format: Roll Number~Full Name
Information about grades
Line format: Course Code~Semester~Year~Roll Number~Grade
The possible grades are A, AB, B, BC, C, CD, D with corresponding grade points 10, 9, 8, 7, 6, 5 and 4. The grade point average of a student is the sum of his/her grade points divided by the number of courses. For instance, if a student has taken two courses with grades A and C, the grade point average is 8 = (10+6)÷2. If a student has not completed any courses, the grade point average is defined to be 0.

You may assume that the data is internally consistent. For every grade, there is a corresponding course code and roll number in the input data.

Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Courses. The second section begins with a line containing Students. The third section begins with a line containing Grades. The end of the input is marked by a line containing EndOfInput.

Write a Python program to read the data as described above and print out a line listing the grade point average for each student in the following format:

Roll Number~Full Name~Grade Point Average
Your output should be sorted by Roll Number. The grade point average should be rounded off to 2 digits after the decimal point. Use the built-in function round().

Here is a sample input and its corresponding output.

Sample Input

Courses
TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
CHAR~Charms~1~2011-2012~Filius Flitwick
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Grades
TRAN~1~2011-2012~SLY2301~AB
TRAN~1~2011-2012~SLY2302~B
TRAN~1~2011-2012~SLY2303~B
TRAN~1~2011-2012~SLY2305~A
TRAN~1~2011-2012~SLY2306~BC
TRAN~1~2011-2012~SLY2308~A
TRAN~1~2011-2012~SLY2309~AB
CHAR~1~2011-2012~SLY2301~A
CHAR~1~2011-2012~SLY2302~BC
CHAR~1~2011-2012~SLY2303~B
CHAR~1~2011-2012~SLY2305~BC
CHAR~1~2011-2012~SLY2306~C
CHAR~1~2011-2012~SLY2307~B
CHAR~1~2011-2012~SLY2308~AB
EndOfInput
Sample Input

SLY2301~Hannah Abbott~9.5
SLY2302~Euan Abercrombie~7.5
SLY2303~Stewart Ackerley~8.0
SLY2304~Bertram Aubrey~0
SLY2305~Avery~8.5
SLY2306~Malcolm Baddock~6.5
SLY2307~Marcus Belby~8.0
SLY2308~Katie Bell~9.5
SLY2309~Sirius Orion Black~9.0
'''

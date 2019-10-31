# Last lecture: Tuples
# Today: Dictionaries and Sets

NAME_INDEX = 0
AGE_INDEX = 1
HEIGHT_INDEX = 2
GRADES_INDEX = 3

students = {}
students['Janice'] = {'age': 18, 'height': 167, 'grades':[87, 88, 85, 41]}

# populate it from a file
fname = 'grades.txt'
file = open(fname, 'r')

attribute_list = file.readline().lower().split()

for i in range(len(attribute_list)):
    attribute_list[i] = attribute_list[i].strip()

for line in file:
    parsed_content = line.split() #splits at whitespace
    student_name = parsed_content[NAME_INDEX].strip() 
    students[student_name] = {}
    for i in range(AGE_INDEX, GRADES_INDEX):
        students[student_name][attribute_list[i]] = parsed_content[i].strip()

    grades = parsed_content[GRADES_INDEX].split(',')
    for i in range(len(grades)):
        grades[i] = float(grades[i])
    students[student_name][attribute_list[-1]] = grades

print(students)     

file.close()

all_student_names = list(students.keys())
num_students = len(all_student_names)
len(students)

anonymized_data = list(students.values())

#  now I want to compute everyone's averages
for student in students:
    students[student]['average'] = sum(students[student][attribute_list[GRADES_INDEX]])/len(students[student][attribute_list[GRADES_INDEX]])

# now what about writing the results to a file?
    

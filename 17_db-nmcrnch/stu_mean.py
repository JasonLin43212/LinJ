#Mai Mushroomz -- Jason Lin, Mai Rachlevsky
#SoftDev1 pd07
#K17 -- Average
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="foo.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

total_grade = []
num_classes = []


command = "SELECT name, peeps.id, mark FROM courses, peeps WHERE peeps.id = courses.id"
c.execute(command)

# When you loop through c, it gives you (name,id,mark)
for row in c:
    if row[1] > len(total_grade):
        total_grade.insert(row[1]-1,row[2])
        num_classes.insert(row[1]-1,1)
    else:
        total_grade[row[1]-1] += row[2]
        num_classes[row[1]-1] += 1

command = "CREATE TABLE peeps_avg(id INTEGER, average INTEGER)"
c.execute(command)

for x in range(len(total_grade)):
    command = "INSERT INTO peeps_avg VALUES({0},{1})".format(x+1,total_grade[x]/num_classes[x])
    c.execute(command)

db.commit()

def addIntoCourse(course_name,grade,student_id):
    command = 'INSERT INTO courses VALUES("{0}",{1},{2})'.format(course_name,grade,student_id)
    c.execute(command)
    db.commit();

addIntoCourse("physics",87,4)

db.close() #close database

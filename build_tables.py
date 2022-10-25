import mysql.connector

conn = mysql.connector.connect(user='root', password='123456', database='project')
cursor = conn.cursor()

# <<< Build database-table-students >>>
cursor.execute('DROP TABLE IF EXISTS `students`;')
cursor.execute('create table students(id int primary key, name varchar(20), email varchar(50))')
name=["Andrew","Brian","Charles","Daniel","Edward","Frank","Gregory","Henry","Ivy","James"]
for i in range(10):
    cursor.execute('insert into students (id, name, email) values (%s,%s,%s)', [i+1, name[i], name[i]+"3278p@gmail.com"])

# <<< Build database-table-courses >>>
cursor.execute('DROP TABLE IF EXISTS `courses`;')
cursor.execute('create table courses(id varchar(20) primary key,'+
                'name varchar(1000), classroom_address varchar(1000), links_of_Zoom varchar(1000))')
courses_id=["2502", "3231", "3235", "3258", "3259", "3270", "3271", "3278", "3314", "3316"]
courses_name=["Computing Fundamentals", "Computer Architecture", 
                "Compiling Techniques", "Functional Programming", 
                "Principles of Programming Languages", "Artificial Intelligence", 
                "Computer Graphics", "Introduction to database management systems", 
                "Machine Learning", "Quantum Information and Computation"]
classroom_address=["LE1","LE2", "LE3", "LE4", "CYPP1", "CYPP2", "MWT1", "MWT2","CYCP1", "CYCP2"]
#links_of_Zoom=[]
for i in range(10):
    cursor.execute('insert into courses (id, name, classroom_address, links_of_Zoom) values (%s,%s,%s,%s)', 
    ["COMP"+courses_id[i], courses_name[i], classroom_address[i], "https://hku.zoom.us/j/96"+str(int(courses_id[i])-1011)+"40999"])

# <<< Build database-table-studentsVScourses >>>
cursor.execute('DROP TABLE IF EXISTS `studentsVScourses`;')
cursor.execute('create table studentsVScourses(studnet_id int, course_id varchar(200))')
for i in range(10):
    for j in range(5):
        cursor.execute('insert into studentsVScourses (studnet_id, course_id) values (%s,%s)', [i+1, "COMP"+courses_id[(i+j)%10]])

conn.commit()
# cursor.execute('select name from students')
# values = cursor.fetchall()
# print(values)
print("tables updated")

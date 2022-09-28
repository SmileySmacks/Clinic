import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database = db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")



create_table1 = """
create table Admissions(
Patient_ID int primary key,
Patient_Name varchar(30) not null,
Patient_DOB varchar(10) not null,
Patient_Insurance varchar(20) not null,
Patient_Phone varchar(25) not null,
Patient_Email varchar(30) not null,
Patient_Reason varchar(40) not null);"""

create_table2 = """
create table Anesthetics_Staff(
Employee_ID int primary key,
Employee_Name varchar(30) not null,
Employee_Education varchar(20) not null,
Employee_Hiring_Date varchar(10) not null,
Employee_Salary varchar(15) not null,
Employee_Schedule varchar(10) not null,
Employee_eBenefits varchar(3) not null);"""

create_table3 = """
create table Cardiology_Staff(
Employee_ID int primary key,
Employee_Name varchar(30) not null,
Employee_Education varchar(20) not null,
Employee_Hiring_Date varchar(10) not null,
Employee_Salary varchar(15) not null,
Employee_Schedule varchar(10) not null,
Employee_eBenefits varchar(3) not null);"""

create_table4 = """
create table September_Cardiology_Appointments(
Appointment_ID int primary key,
Appointment_Date varchar(10) not null,
Appointment_Time varchar(10) not null,
Patient_Name varchar(30) not null,
Doctor_Name varchar(30) not null,
Completed varchar(20) not null);"""

admissions_info = """
insert into Admissions values
( 001, "Mark Blue", "11/06/1988", "Geico", "(111) 111-1111", "patient1@gmail.com", "cough"),
( 002, "Bob Green", "09/16/1978", "Geico", "(111) 111-1112", "patient2@gmail.com", "vomiting"),
( 003, "Tony Red", "12/14/1998", "Advance", "(111) 111-1113", "patient3@gmail.com", "abdominal pain"),
( 004, "Steve Orange", "03/21/1984", "Progressive", "(111) 111-1114", "patient4@gmail.com", "check-up"),
( 005, "Kyle Yellow", "12/15/1975", "Liberty", "(111) 111-1115", "patient5@gmail.com", "cough"),
( 006, "Chris Purple", "11/24/2000", "Advance", "(111) 111-1116", "patient6@gmail.com", "vomiting"),
( 007, "William Violet", "11/20/1996", "Liberty", "(111) 111-1117", "patient7@gmail.com", "abdominal pain"),
( 008, "Mary Pink", "09/30/1998", "Liberty", "(111) 111-1118", "patient8@gmail.com", "check-up"),
( 009, "Stephanie Cyan", "08/23/1969", "Liberty", "(111) 111-1119", "patient9@gmail.com", "cough"),
( 010, "Linda Magenta", "04/15/1997", "Progressive", "(222) 222-2222", "patient10@gmail.com", "vomiting"),
( 011, "Mya Maroon", "05/11/1995", "Advance", "(222) 222-2223", "patient11@gmail.com", "abdominal pain"),
( 012, "Kimberly Sapphire", "10/13/1982", "Advance", "(222) 222-2224", "patient12@gmail.com", "check-up"),
( 013, "Kristina White", "10/06/1991", "Liberty", "(222) 222-2225", "patient13@gmail.com", "cough"),
( 014, "Alex Taupe", "06/04/1987", "Progressive", "(222) 222-2226", "patient14@gmail.com", "vomiting"),
( 015, "Pzal Mahogany", "01/01/2000", "Geico", "(222) 222-2227", "patient15@gmail.com", "abdominal pain"),
( 016, "Kelly Brown", "08/17/1959", "Advance", "(222) 222-2228", "patient16@gmail.com", "check-up"),
( 017, "Brandon Black", "10/15/1998", "Advance", "(222) 222-2229", "patient17@gmail.com", "cough"),
( 018, "Harriot Burgandy", "12/13/1980", "Advance", "(333) 333-3333", "patient18@gmail.com", "vomiting"),
( 019, "Lance Azul", "05/12/1973", "Geico", "(333) 333-3334", "patient19@gmail.com", "abdominal pain"),
( 020, "Marideth Grey", "11/09/1985", "Progressive", "(333) 333-3335", "patient20@gmail.com", "check-up");"""

anesthetics_info = """
insert into Anesthetics_Staff values
( 001, "Manuel Hernandez", "BS", "03/12/2015", "$110,000", "M-F", "Yes"),
( 002, "Timothy Foster", "Masters", "07/29/2019", "$120,000", "M-F", "Yes"),
( 003, "Trevon Archer", "BS", "08/05/2016", "$130,000", "M-F", "Yes"),
( 004, "Cameron Bakehorn", "Masters", "06/11/2016", "$140,000", "M-F", "Yes"),
( 005, "Michael Woodruff", "Masters", "11/30/2012", "$150,000", "M-F", "Yes");"""

cardiology_info = """
insert into Cardiology_Staff values
( 001, "Anton Luna", "Masters", "02/11/2016", "$110,000", "M-F", "Yes"),
( 002, "Sara Gegetskas", "Masters", "07/22/2017", "$120,000", "M-F", "Yes"),
( 003, "Kaitlyn Shipman", "Masters", "04/16/2020", "$130,000", "M-F", "Yes"),
( 004, "Grace Comerford", "Masters", "09/20/2019", "$140,000", "M-F", "Yes"),
( 005, "Tristan Bragg", "Masters", "05/02/2015", "$150,000", "M-F", "Yes");"""

sept_apt_info = """
insert into September_Cardiology_Appointments values
( 001, "09/01/2022", "0830", "Mark Blue", "Timothy Foster", "Yes"),
( 002, "09/03/2022", "0830", "Bob Green", "Trevon Archer", "Yes"),
( 003, "09/05/2022", "0830", "Tony Red", "Cameron Bakehorn", "Yes"),
( 004, "09/07/2022", "0830", "Steve Orange", "Manuel Hernandez", "Yes"),
( 005, "09/09/2022", "0830", "Kyle Yellow", "Michael Woodruff", "Yes"),
( 006, "09/11/2022", "0830", "Chris Purple", "Timothy Foster", "Yes"),
( 007, "09/13/2022", "0830", "William Violet", "Anton Luna", "Yes"),
( 008, "09/15/2022", "0830", "Mary Pink", "Sara Gegetskas", "Yes"),
( 009, "09/17/2022", "0830", "Stephanie Cyan", "Manuel Hernandez", "Yes"),
( 010, "09/19/2022", "0830", "Linda Magenta", "Kaitlyn Shipman", "No"),
( 011, "09/21/2022", "0830", "Mya Maroon", "Grace Comerford", "No"),
( 012, "09/23/2022", "0830", "Kimberly Sapphire", "Tristan Bragg", "No"),
( 013, "09/25/2022", "0830", "Kristina White", "Tristan Bragg", "No"),
( 014, "09/27/2022", "0830", "Alex Taupe", "Timothy Foster", "No"),
( 015, "09/29/2022", "0830", "Pzal Mahogany", "Cameron Bakehorn", "No"),
( 016, "09/31/2022", "0830", "Kelly Brown", "Grace Comerford", "No");"""


display_table1 = """
select * from Admissions;"""

display_table2 = """
select * from Anesthetics_Staff;"""

display_table3 = """
select * from Cardiology_Staff;"""

display_table4 = """
select * from September_Cardiology_Appointments;"""

connection = create_server_connection("localhost", "root", "student", "Central_Clinic")
execute_query(connection, sept_apt_info)

information = read_query(connection, display_table4)
for values in information:
    print(values)


import utils
from datetime import datetime

class Student:
    @staticmethod
    def load_student_data(student_id):
        q='''Select *
            from Student
            WHERE Student_Id = ?'''
        data=utils.query_db(q,(student_id,),1)
        if not data:
            return None
        return {
            "Student_Id" : data[0],
            "NAME" : data[1],
            "Age" : data[2],
            "Gender" : data[3],
            "Class": data[4],
            "Grade": data[5],
            "Email": data[6],
            "Contact" : data[7],
            "Login_Id" : data[8],
            "Password" : data[9]
        }
    @staticmethod
    def student_login(): 
        student_id=(input("ENTER YOUR STUDENT ID : "))
        data = Student.load_student_data(student_id)
        if not data:
            print("ASK ADMIN TO CREATE A STUDENT")
            return False
        logid= input("ENTER YOUR LOGIN ID : " )
        password=input("ENTER YOUR PASSWORD : ")
        if logid==data["Login_Id"] and password==data["Password"]:
            print("LOGIN Successful! ")
            Student.dashboard_student(data)
            return True
        else:print("INVALID CREDENTIALS")
    @staticmethod
    def see_marks(student_id):
        q=''' Select *
              from Marks
              Where Student_Id =?'''
        data=utils.query_db(q, (student_id,),2)
        print("\n--_MARKS---")
        marks_n=["Unit_Test1","Midterm","Unit_Test2","Preliminary","Finals"]    
        for idx, row in enumerate(data, 1):
                print(f"{idx}. Student_Id : {row[0]}")
                for i, marks_n in enumerate(marks_n):
                    val=row[i+1]
                    if val is not None and val!="":
                        print(f" {marks_n} : {val}")
    @staticmethod
    def see_attendance(student_id):
        q=''' Select *
              from Attendance
              Where Student_Id =?'''
        data=utils.query_db(q, (student_id,),2)
        print("\n--ATTENDANCE---")
        months=["January", "February", "March", "April", 
                "May", "June", "July", "August", 
                        "September", "October", "November", "December"]    
        for idx, row in enumerate(data, 1):
                print(f"{idx}. Student_Id : {row[0]}")
                for i, month in enumerate(months, start=1):
                    if row[i] is not None:
                        print(f"{month} : {row[i]}")

    @staticmethod
    def message(student_id):
        message=input("ENTER YOUR MESSAGE : ")
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        q=''' insert into message
        (Student_id,Date,Time,Message)
        Values(?,?,?,?)
        '''
        d=(student_id,current_date,current_time,message)
        utils.query_db(q,d,0)

    @staticmethod
    def see_details(student_id):
        q=''' Select *
              from Student
              Where Student_Id =?'''
        data=utils.query_db(q, (student_id,),2)
        print("\n--DETAILS---")    
        for idx, data in enumerate(data, 1):
            print(f"{idx}. Student_Id : {data[0]}\n  Student_Name : {data[1]}\n  Age : {data[2]}\n",end="")
            print(f" Gender : {data[3]}\n  Class : {data[4]}\n  Grade : {data[5]}\n  Email : {data[6]}\n",end="")
            print(f" Contact : {data[7]}\n  Login_Id : {data[8]}\n  Password : {data[9]}")
        print()
        q=''' Select *
            from Subjects
            Where Student_Id =?'''
        data=utils.query_db(q, (student_id,),2)
        print("\n--SUBJECT DETAILS---")    
        for idx, data in enumerate(data, 1):
            print(f"{idx}. Student_Id : {data[0]}\n  Subject_1 : {data[1]}\n  Subject_2 : {data[2]}\n",end="")
            print(f" Subject_3 : {data[3]}\n  Subject_4 : {data[4]}\n  Subject_5 : {data[5]}")
    @staticmethod
    def password_change(student_id):
        p = input("Enter new Password : ")
        q=''' update Student
            set Password =?
            WHERE Student_Id=?'''
        d=(p,student_id)
        utils.query_db(q,d,0)
    
    @staticmethod
    def dashboard_student(data):
        c=0
        while c!=6:
            print("--- Student Menu ---")
            print("1.SEE MARKS")
            print("2.SEE ATTENDANCE")
            print("3.SEE YOUR FULL DETAIL")
            print("4.MESSAGE ADMIN")
            print("5.PASSWORD CHANGE")
            print("6.LOGOUT")            
            c= int(input("Select an option (1-5): "))
            if c==1:Student.see_marks(data["Student_Id"])
            elif c==2:Student.see_attendance(data["Student_Id"])
            elif c==3:Student.see_details(data["Student_Id"])
            elif c==4:Student.message(data["Student_Id"])
            elif c==5:Student.password_change(data["Student_Id"])
    @staticmethod
    def main2():
        Student.student_login()
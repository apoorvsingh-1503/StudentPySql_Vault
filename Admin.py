import utils

chec= 54864
class Admin:
    @staticmethod
    def load_admin_data(admin_id):
        q='''Select *
            from Admin
            WHERE Admin_Id = ?'''
        data=utils.query_db(q,(admin_id,),1)
        if not data:
            return None
        return {
            "Admin_NAME" : data[1],
            "Login_Id" : data[2],
            "Password" : data[3],
        }
    @staticmethod
    def admin_creation():
        q=" select count (*) from Admin"
        c=utils.query_db(q,a=1)
        ch=c[0]
        name=input("ENTER YOUR NAME : ")
        logid=name+"2026"
        password=5667
        Adminid="APS-AD-"+str(1000+ch)
        qu=''' insert into Admin
            (Admin_Id,Name,Login_Id,Password)
            Values(?,?,?,?)
            '''
        d=(Adminid,name,logid,password)
        utils.query_db(qu, d, 0)
        print("DETAILS-----")
        print(f"ADMIN ID : {Adminid}")
        print(f"NAME : {name}")
        print(f"LOGIN ID : {logid}")
        print(f"PASSWORD : {password}")
        print(f"CHECKER ID : {chec}")
        
    @staticmethod
    def admin_login():
        q=''' select count(*)
              from Admin
           '''
        c=utils.query_db(q,None,1)[0]
        if c==0:
            print("NO ADMIN FOUND CREATE ONE")
            Admin.admin_creation()
        else: 
            admin_id=input("ENTER YOUR ADMIN ID : ").upper()
            logid= input("ENTER YOUR LOGIN ID : " )
            password=input("ENTER YOUR PASSWORD : ")
            data= Admin.load_admin_data(admin_id)
            if logid!=data["Login_Id"] and password!=data["Password"]:
                print("INVALID CREDENTIALS")
                return False
            else:
                print("LOGIN Successful! ")
                Admin.dashboard_admin()
                print("INVALID CREDENTIALS")
    @staticmethod
    def add_admin():
        ch= int(input("ENTER YOUR CHECKER ID : "))
        if ch==chec:
            Admin.admin_creation()
        else:print("INVALID CHECKER ID")
    @staticmethod
    def student_creation():
        q=" select count (*) from Student"
        c=utils.query_db(q,a=1)[0]
        name=input("ENTER NAME OF STUDENT : ")
        age=int(input("ENTER STUDENT'S AGE : "))
        gen=input("ENTER STUDENT'S GENDER : ")
        cl=int(input("ENTER STUDENTS CLASS : "))
        sec=input("ENTER STUDENT'S SECTIONS :  ")
        email=input("ENTER STUDENTS EMAIL ID : ")
        con=input("ENTER STUDENTS CONTACT NUMBER : ")
        Studentid="APS-ST-"+str(1000+c)
        logid=name+str(cl)+"2026"
        password=1234
        raw=(Studentid,name,age,gen,cl,sec,email,con,logid,password)
        q=''' insert into Student
            (Student_Id,Name,Age,Gender,Class,Grade,Email,Contact,Login_Id,Password)
            VALUES(?,?,?,?,?,?,?,?,?,?)'''
        utils.query_db(q,raw,0)
        print("STUDENT DETAILS---------")
        print(f"NAME: {name}")
        print(f"AGE: {age}")
        print(f"GENDER: {gen}")
        print(f"CLASS: {cl}")
        print(f"SECTION: {sec}")
        print(f"EMAIL: {email}")
        print(f"CONTACT: {con}")
        print(f"STUDENT_ID: {Studentid}")
        print(f"LOG_ID: {logid}")
        print(f"PASSWORD: {password}")

    @staticmethod
    def delete_student():
        id=input("ENTER STUDENT ID OF THE STUDENT TO BE DELETED : ").upper()
        utils.query_db('''DELETE FROM Student WHERE Student_Id = ?''', (id,),0)
        print("STUDENT DELETED")

    @staticmethod
    def add_subjects():
        id=input("ENTER STUDENT ID OF THE STUDENT WHOOSE SUBJECTS TO BE ADDED : ").upper()
        q='''select Student_Id from Student Where Student_Id=?'''
        ch=utils.query_db(q,(id,),1)
        if not ch:
            print("NO SUCH STUDENT FOUND")
            return
        s1=input("ENTER NAME OF SUBJECT 1 : ")
        s2=input("ENTER NAME OF SUBJECT 2 : ")
        s3=input("ENTER NAME OF SUBJECT 3 : ")
        s4=input("ENTER NAME OF SUBJECT 4 : ")
        s5=input("ENTER NAME OF SUBJECT 5 : ")
        q=''' insert into Subjects
              (Student_Id,Subject_1,Subject_2,Subject_3,Subject_4,Subject_5)
              Values(?,?,?,?,?,?)
             '''
        raw=(id,s1,s2,s3,s4,s5)
        utils.query_db(q,raw,0)
        print("SUBJECTS ADDED SUCCESFULY!")

    @staticmethod
    def add_marks():
        id=input("ENTER STUDENT ID OF THE STUDENT WHOOSE SUBJECTS TO BE ADDED : ").upper()
        q=''' Select * from Student
              Where Student_Id=?'''
        data=utils.query_db(q,(id,),1)
        if not data:
            print("NO SUCH STUDENT FOUND")
            return
        ut1=input("ENTER TOTAL MARKS IN UNIT TEST 1 : ")
        mid=input("ENTER TOTAL MARKS IN MIDTERM : ")
        ut2=input("ENTER TOTAL MARKS IN UNIT TEST 2 : ")
        pre=input("ENTER TOTAL MARKS IN PRELIMINARY : ")
        final=input("ENTER TOTAL MARKS IN FINALS : ")
        qu = ''' INSERT OR REPLACE INTO Marks 
             (Student_Id,Unit_Test1, Midterm, Unit_Test2, Preliminary, Finals)
             VALUES (?, ?, ?, ?, ?, ?)'''
        d=(id,ut1,mid,ut2,pre,final)
        utils.query_db(qu,d, 0)
        print("MARKS ADDED SUCCESSFULY!")

    @staticmethod
    def update_attendance():
        id=input("ENTER STUDENT ID OF THE STUDENT WHOOSE ATTENDANCE TO BE ADDED : ").upper()
        q=''' Select * from Student
              Where Student_Id=?'''
        data=utils.query_db(q,(id,),1)
        if not data:
            print("NO SUCH STUDENT FOUND")
            return
        month=input("ENTER MONTH WHOSE ATTENFANCE TO BE UPDATED : ").capitalize()
        att=int(input("ENTER TOTAL NUMBER OF DAYS PRESENT : "))
        q=f''' insert into Attendance
                (Student_Id,{month})
                Values(?,?)
            '''
        utils.query_db(q,(id,att,),0)
        print("ATTENDANCE UPDATED SUCCESFULY!")
    @staticmethod
    def password_change():
        adminid=input("ENTER YOUR ADMIN ID : ").upper()
        p = input("Enter new Password : ")
        q=''' update Admin
            set Password =?
            WHERE Admin_Id=?'''
        d=(p,adminid)
        utils.query_db(q,d,0)   
    @staticmethod
    def see_message():
        q=''' select *
              from Message
          '''
        data= utils.query_db(q,None,2)    
        print("\n---MESSAGE---")    
        for idx, data in enumerate(data, 1):
            print(f"{idx}. Student_Id: {data[0]}\nDATE: {data[1]}\nTIME: {data[2]}\nMessage: {data[3]}")
    @staticmethod
    def dashboard_admin():
        c=0
        while c!=8:
            print("1.ADD STUDENT")
            print("2.ADD STUDENT ATTENDANCE")
            print("3.ADD STUDENT'S SUBJECTS")
            print("4.ADD STUDENT'S MARKS")
            print("5.DELETE STUDENT")
            print("6.SEE STUDENT MESSAGE")
            print("7.ADD ADMIN")
            print("8.CHANGE PASSWORD")
            print("9.LOGOUT")
            c=int(input("Select an option (1-8): "))
            if   c==1:Admin.student_creation()
            elif c==2:Admin.update_attendance()
            elif c==3:Admin.add_subjects()
            elif c==4:Admin.add_marks()
            elif c==5:Admin.delete_student()
            elif c==6:Admin.see_message()
            elif c==7:Admin.add_admin()
            elif c==8:Admin.password_change()
    @staticmethod
    def main1():
        Admin.admin_login()
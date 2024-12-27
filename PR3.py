studentRecords = [{'StudentID': 1, 'Name': 'Namya', 'Age': 18, 'Grade': 'B+', 'Date of birth': '2006-08-05', 'Subjects': {'CPPM', 'Maths', 'ss'}}, {'StudentID': 2, 'Name': 'Yud', 'Age': 19, 'Grade': 'A++', 'Date of birth': '2006-25-06', 'Subjects': {'DPA', 'Accounts', 'Maths'}}, {'StudentID': 3, 'Name': 'Jugal', 'Age': 20, 'Grade': 'A+', 'Date of birth': '2006-25-08', 'Subjects': {'Accounts'}}]
while True :
    print("{(Welome to student data organizer!)}")
    print("1.Add student")
    print("2.Display all student")
    print("3.update student information")
    print("4.delete student")
    print("5.display subjects offered")
    print("6.Exit")
    print("_____________________________________________________________________")
    select = int(input("Enter your choice = "))
    print("_____________________________________________________________________")

    if select==1 :
        information = {}
        print("Enter Student Details")
        Student_ID = int(input("Student ID = "))
        Name = input("Name = ")
        Age = int(input("Age = "))
        Grade = input("Grade = ")
        DOB = input("Date of birth(YYYY-MM-DD) = ")
        Subjects = input("Subjects(comma-separated) = ")
        information["StudentID"] = Student_ID
        information["Name"] = Name
        information["Age"] = Age
        information["Grade"] = Grade
        information["Date of birth"] = DOB
        information["Subjects"] = set(Subjects.split(","))
        studentRecords.append(information)
        print(studentRecords)
        print("_____________________________________________________________________")
        
    elif select==2 :
        for i in studentRecords :
            print("_____________________________________________________________________")
            print("Student_ID = ",i["StudentID"])
            print("Name = ",i["Name"])
            print("Age = ",i["Age"])
            print("Grade = ",i["Grade"])
            print("DOB = ",i["Date of birth"])
            print("Subjects = ",i["Subjects"])
            print("_____________________________________________________________________")
            
    elif select==3 :
        information = {}
        c = 0
        StudentID = int(input("Enter the ID = "))
        for i in studentRecords :
            if i["StudentID"]==StudentID :
                print("student Found")
                Name = input("Name = ")
                Age = int(input("Age = "))
                Grade = input("Grade = ")
                Subjects = input("Subjects(comma-separated) = ")
                information["StudentID"] = i["StudentID"]
                information["Name"] = Name
                information["Age"] = Age
                information["Grade"] = Grade
                information["Date of birth"] = i["Date of birth"]
                information["Subjects"] = set(Subjects.split(","))
                studentRecords[c] = information
                print(studentRecords)
                print("Student updated successfully")
                print("_____________________________________________________________________")
                break
            c = c+1
        else :
            print("Not Found")
    elif select==4 :
        c = 0
        choice = int(input("Enter your choice to delete student ID = "))
        for i in studentRecords :
            if i["StudentID"]==choice :
                studentRecords.remove(i)
                print("Student data Successfully deleted")
                print("_____________________________________________________________________")
                break 
            c = c+1
        else :
            print("Student data Not Found")
            print("_____________________________________________________________________")
    elif select==5 :
        for i in studentRecords :
            print("_____________________________________________________________________")
            print("Name = ",i["Name"])
            print("Subjects = ",i["Subjects"])
            print("_____________________________________________________________________")
    elif select==6 :
        print("(byeee!!)")
        break
    else :
        print("Invalid Input")
        print("_____________________________________________________________________")
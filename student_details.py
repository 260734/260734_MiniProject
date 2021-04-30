def addRecord():
    import pickle
    rno = int(input("Enter Roll no. :"))
    name = input("Enter name:")
    cls = int(input("Enter class:"))
    sec = input("Enter Section of class:")
    marks = int(input("Enter total marks:"))
    stu = {"RollNo": rno, "Name": name, "Class": cls, "Section": sec, "Total Marks": marks}
    f = open("StudentData.dat", "ab")
    pickle.dump(stu, f)
    f.close()
    print("One student record added successfully")

def displayRecord():
    import pickle
    f = open("StudentData.dat", "rb")
    while True:
        try:
            stu = pickle.load(f)
            print("RollNo:", stu["RollNo"])
            print("Name:", stu["Name"])
            print("Class:", stu["Class"])
            print("Section:", stu["Section"])
            print("Total Marks:", stu["Total Marks"])
        except EOFError:
            print("File is empty. No Record present")
            break
    f.close()

def searchRecord(r):
    import pickle
    f = open("StudentData.dat", "rb")
    found = False
    while True:
        try:
            stu = pickle.load(f)
            if stu["RollNo"] == r:
                print("RollNo:", stu["RollNo"])
                print("Name:", stu["Name"])
                print("Class:", stu["Class"])
                print("Section:", stu["Section"])
                print("Total Marks:", stu["Total Marks"])
                found = True
        except EOFError:
            break
    if found == False:
        print("No student data found", r)
    f.close()

def updateMarks(r, m):
    import pickle
    f = open("StudentData.dat", "rb")
    stuLst = []
    while True:
        try:
            stu = pickle.load(f)
            stuLst.append(stu)
        except EOFError:
            break
    f.close()

    for i in range(len(stuLst)):
        if stuLst[i]["RollNo"] == r:
            stuLst[i]["Total Marks"] = m

    f = open("StudentData.dat", "wb")
    for x in stuLst:
        pickle.dump(x, f)
    print("Marks updated Successfully")
    f.close()

def deleteRecord(r):
    import pickle
    f = open("StudentData.dat", "rb")
    stuLst = []
    while True:
        try:
            stu = pickle.load(f)
            stuLst.append(stu)
        except EOFError:
            break
    f.close()
    ans = input("are you sure to delete student record!(Y/y for YES")
    if ans == 'Y' or ans == 'y':
        f= open("StudentData.dat", "wb")
        for x in stuLst:
            if x["RollNo"] == r:
                continue
            pickle.dump(x, f)
        print("one student record deleted successfully")
        f.close()

while True:
    print("\nType 1 to add new student to data")
    print("\nType 2 to display all student data")
    print("\nType 3 to search student data")
    print("\nType 4 to update student data")
    print("\nType 5 to delete student data")
    choice = int(input("Enter your choice"))
    if choice == 1:
        addRecord()
    elif choice == 2:
        displayRecord()
    elif choice == 3:
        r = int(input("Enter roll no. to search"))
        searchRecord(r)
    elif choice == 4:
        r = int(input("Enter roll no. of student to update"))
        m = int(input("enter new marks"))
        updateMarks(r, m)
    elif choice == 5:
        r = int(input("Enter roll no. delete record"))
        deleteRecord(r)
    else:
        break
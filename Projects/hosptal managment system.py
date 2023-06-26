import os
import csv
#Function to add a new patient
def newPatient():
    print("Add a new Patient Record")
    print("=========================")
    f=open('Patient.csv','a',newline='\r\n')
    s=csv.writer(f)
    Patientid=input('Enter Patient id:')
    Patientname=input('Enter Patient name:')
    Disease=input('Enter Disease:')
    fee=float(input('Enter Fee:'))
    Doctorname=input('Enter name of Doctor:')
    print("----------------------------------------------------")
    rec=[Patientid,Patientname,Disease,fee,Doctorname]
    s.writerow(rec)
    f.close()
    print("Patient Record Saved")
    input("Press any key to continue..")

#Function to adit patient data
def editPatient():
    print("Modify a Patient Record")
    print("=========================")
    f=open('Patient.csv','r',newline='\r\n') 
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter Patientid whose record you want to modify:')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("-------------------------------")
            print("Patient id:",rec[0])
            print("Patient Name:",rec[1])
            print("Disease;",rec[2])
            print("Fee:",rec[3])
            print("Name of Doctor:",rec[4])
            print("-------------------------------")
            
            choice=input("Do you want to modify this Patient Record(y/n):")
            if choice=='y' or choice=='Y':
                print("----------------------------------------------------")
                Patientid=input('Enter new Patient id:')
                Patientname=input('Enter new Patient name:')
                Disease=input('Enter Disease:')
                fee=float(input('Enter Fee:'))
                Doctorname=input('Enter name of Doctor:')
                print("----------------------------------------------------")
                rec=[Patientid,Patientname,Disease,fee,Doctorname]
                s1.writerow(rec)
                print("Patient Record Modified")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()   
    f1.close()
    os.remove("Patient.csv")
    os.rename("temp.csv","Patient.csv")
    
    input("Press any key to continue..")

#Function to delete patient data 
def delPatient():
    f=open('Patient.csv','r',newline='\r\n') 
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter Patientid whose record you want to delete:')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("-------------------------------")
            print("Patient id:",rec[0])
            print("Patient Name:",rec[1])
            print("Disease:",rec[2])
            print("Fee:",rec[3])
            print("Name of Doctor:",rec[4])
            print("-------------------------------")
            choice=input("Do you want to delete this Patient Record(y/n):")
            if choice=='y' or choice=='Y':
                pass
                print("Patient Record Deleted....")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("Patient.csv")
    os.rename("temp.csv","Patient.csv")
    input("Press any key to continue..")

#Function to search patient data using patient id
def searchPatient():
    print("Search a Patient Record:")
    print("=====================")
    f=open('Patient.csv','r',newline='\r\n')  
    r=input('Enter Patientid you want to search:')
    s=csv.reader(f)
    for rec in s:
        if rec[0]==r:
            print("-------------------------------")
            print("Patient id:",rec[0])
            print("Patient Name:",rec[1])
            print("Disease:",rec[2])
            print("Fee:",rec[3])
            print("Name of Doctor:",rec[4])
            print("-------------------------------")
    f.close()
    input("Press any key to continue..")

#Function to display the full list of the patients
def listofPatients():
    print("========================================================================================")
    print("                 List of All Patients")
    print("========================================================================================")
    f=open('Patient.csv','r',newline='\r\n')  
    s=csv.reader(f)
    i=1
    for rec in s:
        print(rec[0],end="\t\t")
        print(rec[1],end="\t\t")
        print(rec[2],end="\t\t")
        print(rec[3],end="\t\t")
        print(rec[4])
        i+=1
    f.close()
    print("----------------------------------------------------------------------------------------")
    input("Press any key to continue..")

#Menu of the functions avialable
def menu():
    choice=0
    while choice!=6:
        print("\n")
        print("|--------------------------|")
        print("| Hospital Management System |")
        print("| -------------------------|")
        print('\n')
        print("########################")
        print("          Menu")
        print("########################")
        print("1. Add a new Patient Record")
        print("2. Modify Existing Patient ")
        print("3. Delete Existing Patient ")
        print("4. Search a Patient")
        print("5. List all Patients")
        print("6. Exit")
        print("-------------------------------")
        choice=int(input('Enter your choice(Please enter the number only):'))
        print("-------------------------------")
        if choice==1:
            newPatient()
        elif choice==2:
            editPatient()
        elif choice==3:
            delPatient()
        elif choice==4:
            searchPatient()
        elif choice==5:
            listofPatients()
        elif choice==6:
            print("Software Exited..")
            break
menu()

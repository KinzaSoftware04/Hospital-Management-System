def add_patient():
    name = input("Enter the patient name please")
    disease = input("Enter the patient disease please")
    check_up_fee = int(input("Enter the patient check up fees please"))
    patient_data = {"name": name ,"disease": disease,"check_up_fee":check_up_fee}
    with open("hopital_records.txt","a") as file:
        file.write(f"Name:{patient_data['name']} , Disease:{patient_data['disease']} , Fees:{patient_data['check_up_fee']} \n")
def view_all_patients():
 try:
     with open("hopital_records.txt","r") as file:
        all_data = file.read()
        print("------- All Patient Record---------------")
        print(all_data)
 except FileNotFoundError:
    print("No file found! Hospital database file is empty")
while True:
    print("-----Hospital Management System-------")
    print("1. add new patient")
    print("2. view all patient")
    print("3. exit software")
    choice = input("Enter your choice from 1 to 3 ")
   
    if choice == "1":
        add_patient()
    elif choice == "2":
        view_all_patients()
    elif choice == "3":
        print("3 detected")
        print("Thankyou for using our sdystem. good by!")
        break
    else:
       print("invalid choice")


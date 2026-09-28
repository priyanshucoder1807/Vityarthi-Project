import datetime
Appointments = []
Departments = {
    "1": {"Name": "General Medicine", "Fees": 500},
    "2": {"Name": "Cardiology", "Fees": 1000},
    "3": {"Name": "Orthopedics", "Fees": 800},
    "4": {"Name": "Pediatrics", "Fees": 600},
    "5": {"Name": "Dermatology", "Fees": 900}
}

Time_Slots = ["9:00 AM", "10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM", "4:00 PM"]

def Display_Welcome():
    print("="*50)
    print(" WELCOME TO VIT BHOPAL HEALTH CENTRE ")
    print("="*50)

def Display_Departments():
    print("\n---AVAILABLE DEPARTMENTS---")
    for key, Dept in Departments.items():
        print(f"{key}. {Dept['Name']} - Fees:₹{Dept['Fees']}")

def Get_Student_Details():
    print("\n---STUDENT DETAILS---")
    Name = input("Enter Your Name: ").strip()
    while not Name:
        print("Please Enter a Name!!")
        Name = input("Enter Your Name: ").strip()
    Reg_Number = input("Enter your Registration Number: ").strip()
    while not Reg_Number:
        print("Please enter your registration number!!")
        Reg_Number = input("Enter your Registration Number: ").strip()
    Age = int(input("Enter your age: "))
    while Age <= 0:
        print("Please enter your age!!")
        Age = int(input("Enter your age: "))
    Mobile_Number = int(input("Enter your Mobile_Number: "))
    while Mobile_Number <= 0:
        print("Please enter your Mobile_Number!!")
        Mobile_Number = int(input("Enter your Mobile_Number: "))
    return {"Name": Name, "Registration Number": Reg_Number, "Age": Age, "Contact Number": Mobile_Number}

def Select_Department():
    Display_Departments()
    Choice = input("\n Select Department(1-5):").strip()
    while Choice not in Departments:
        print("Invalid Choice! Please select a valid department.")
        Choice = input("\n Select Department(1-5):").strip()
    return Choice

def Display_Time_Slot():
    print("\n--- AVAILABLE TIME SLOTS---")
    for i, slot in enumerate(Time_Slots, 1):
        print(f"{i}.{slot}")

def Select_Time_Slot():
    Display_Time_Slot()
    Choice = input("\n---SELECT TIME SLOT--- (1-6):").strip()
    while not Choice.isdigit() or int(Choice) < 1 or int(Choice) > len(Time_Slots):
        print("Invalid choice! Please select a valid time slot.")
        Choice = input("\n---SELECT TIME SLOT--- (1-6):").strip()
    return Time_Slots[int(Choice) - 1]

def Get_appointment_Date():
    print("\n---SELECT DATE---")
    today = datetime.date.today()
    print(f"Today's Date: {today.strftime('%d-%m-%Y')}")
    while True:
        date_input = input("Enter appointment date (DD-MM-YYYY): ").strip()
        try:
            day, month, year = date_input.split('-')
            apt_date = datetime.date(int(year), int(month), int(day))
            if apt_date < today:
                print("Cannot book appointment for past dates!")
                continue
            return apt_date.strftime('%d-%m-%Y')
        except ValueError:
            print("Invalid date format! Please use DD-MM-YYYY")

def Display_Appointment_Summary(Appointment):
    print("\n" + "="*50)
    print("   APPOINTMENT BOOKED SUCCESSFULLY!")
    print("="*50)
    print(f"\nPatient Name: {Appointment['patient']['Name']}")
    print(f"Age: {Appointment['patient']['Age']}")
    print(f"Phone: {Appointment['patient']['Contact Number']}")
    print(f"\nDepartment: {Appointment['department']}")
    print(f"Date: {Appointment['date']}")
    print(f"Time: {Appointment['time']}")
    print(f"\nConsultation Fee: ₹{Appointment['fee']}")
    print(f"Appointment ID: {Appointment['id']}")
    print("\n" + "="*50)
    print("Please arrive 15 minutes before your appointment.")
    print("="*50)

def View_All_Appointments():
    if not Appointments:
        print("\nNo appointments booked yet")
        return
    print("\n" + "="*50)
    print("   ALL APPOINTMENTS")
    print("="*50)
    for apt in Appointments:
        print(f"\nID: {apt['id']}")
        print(f"Student: {apt['patient']['Name']} (Age: {apt['patient']['Age']})")
        print(f"Department: {apt['department']}")
        print(f"Date: {apt['date']} at {apt['time']}")
        print(f"Fee: ₹{apt['fee']}")
        print("-" * 50)

def Book_Appointment():
    Student = Get_Student_Details()
    Dept_Choice = Select_Department()
    Apt_Date = Get_appointment_Date()
    Apt_Time = Select_Time_Slot()
    NewAppointment = {
        "id": f"APT{len(Appointments) + 1001}",
        "patient": Student,
        "department": Departments[Dept_Choice]["Name"],
        "date": Apt_Date,
        "time": Apt_Time,
        "fee": Departments[Dept_Choice]["Fees"]
    }
    Appointments.append(NewAppointment)
    Display_Appointment_Summary(NewAppointment)

def Main():
    Display_Welcome()
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Book New Appointment")
        print("2. View All Appointments")
        print("3. View Department Fees")
        print("4. Exit")
        Choice = input("\n Enter your Choice (1-4):").strip()
        if Choice == "1":
            Book_Appointment()
        elif Choice == "2":
            View_All_Appointments()
        elif Choice == "3":
            Display_Departments()
        elif Choice == "4":
            print("\nThank you for using Vit Bhopal Health Centre!")
            print("Stay healthy! 🏥")
            break
        else:
            print("\n Invalid Choice! Please try again.")

if __name__ == "__main__":
    Main()
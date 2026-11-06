'''
2.	Hospital Management System: Patient Registration (Dictionary), (user input)
Appointment Scheduling (List), Medical Records Storage (File Handling),
 Doctor Information (Tuple), Billing System (Class and Object), 
 Report Generation (Python Libraries)
'''
def patient_registration():
    patient = {}
    patient['name'] = input("Enter patient name: ")
    patient['age'] = int(input("Enter patient age: "))
    patient['gender'] = input("Enter patient gender: ")
    patient['contact'] = input("Enter patient contact number: ")
    return patient
def appointment_scheduling():
    appointments = []
    num_appointments = int(input("Enter number of appointments to schedule: "))
    for i in range(num_appointments):
        appointment_date = input(f"Enter date for appointment {i+1} (YYYY-MM-DD): ")
        doctor_name = input(f"Enter doctor's name for appointment {i+1}: ")
        appointments.append((appointment_date, doctor_name))
    return appointments
def store_medical_records(patient):
    filename = f"{patient['name'].replace(' ', '_')}_medical_records.txt"
    with open(filename, 'w') as file:
        file.write("Medical Records\n")
        file.write(f"Patient Name: {patient['name']}\n")
        file.write(f"Age: {patient['age']}\n")
        file.write(f"Gender: {patient['gender']}\n")
        file.write(f"Contact: {patient['contact']}\n")
        file.close()
def doctor_information():
    doctors = (
        ("Dr. Smith", "Cardiologist"),
        ("Dr. Johnson", "Neurologist"),
        ("Dr. Williams", "Pediatrician"),
        ("Dr. Brown", "Dermatologist")
    )
    
    return doctors
class BillingSystem:
    def __init__(self):
        self.bill_items = []
    
    def add_item(self, description, amount):
        self.bill_items.append((description, amount))
    
    def generate_bill(self):
        total_amount = sum(amount for _, amount in self.bill_items)
        print("\nBilling Summary")
        for description, amount in self.bill_items:
            print(f"{description}: ${amount:.2f}")
        print(f"Total Amount: ${total_amount:.2f}")
def generate_report(patient, appointments, doctors):
    print("\nPatient Report")
    print(f"Name: {patient['name']}")
    print(f"Age: {patient['age']}")
    print(f"Gender: {patient['gender']}")
    print(f"Contact: {patient['contact']}")
    print("\nAppointments:")
    for date, doctor in appointments:
        print(f"Date: {date}, Doctor: {doctor}")
  

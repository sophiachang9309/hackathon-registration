#Name: Sophia Chang
#AM

#tuple holding fized workshop options
workshops = ("Game Design", "AI Chatbots", "Robotics")

#dictionary that uses student names as keys and assigned workshops as values.
registrations = {
    "maya": "Game Design",
    "jordan": "AI Chatbots",
    "alex": "Robotics",
    "sam": "Game Design",
    "taylor": "AI Chatbots"
}

#set that holds the names of students who are currently checked in
checked_in = set()

#menu
print("========== HACKATHON CHECK-IN ==========")
print()
print("1. View Workshops")
print("2. Look Up a Registration")
print("3. Check In a Student")
print("4. View Attendance Report")
print("5. Remove One Check-In")
print("6. Clear All Check-Ins")
print("7. Register a New Student")
print("8. Change a Student's Workshop")
print("9. View Check-Ins for One Workshop")
print("10. Exit")
print()
choice = int(input("Enter your choice: "))

#option 1
def workshop(workshops):
    #for loop to print the workshops
    for i in range(len(workshops)):
        print(f"{i+1}. {workshops[i]}")

#option 2
def reg(workshops):
    #Converts everything into lower case and gets rid of extra spacing
    name = input("Enter student name:").strip().lower()

    #determines if the name is actually found in the registration
    control = False

    #for loop that searches whether or not the name of the student is in the registration
    for n in workshops.items():
        if n[0] == name:
            print("Workshop:", n[1])
            control = True

    #functions when the student isn't found
    if control == False:
        print("Student not found.")

    return name

#option 3
def check_in(name):
    reg()
    if name in checked_in:
        print("This student is already checked in.")
    else:
        checked_in.add(name)
        print("This student has now been checked in.")

#option 4
def report(registrations, checked_in):
    #gets only the keys and convert them into a set
    reg_set = set(registrations)

    #prints the report
    print("========== ATTENDANCE REPORT ==========")
    print()
    print("Registered students:", len(reg_set))
    print("Checked in:", len(checked_in))
    print("Still waiting for:", len(reg_set) - len(checked_in))
    print()

    #checks whether everyone was checked in
    if len(reg_set) == len(checked_in):
        print("Everyone is checked in!")
    else:
        #prints the different 
        print(checked_in.difference(registrations))

#option 5
def remove():
    removed = checked_in.pop()
    return removed
    
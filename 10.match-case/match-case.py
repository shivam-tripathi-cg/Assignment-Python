# Q1
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Pasta")
    case 4:
        print("You selected Sandwich")
    case _:
        print("Invalid Menu Choice")

# Q2
choice = int(input("Enter choice: "))
match choice:
    case 1:
        print("Wi-Fi Selected")
    case 2:
        print("Bluetooth Selected")
    case 3:
        print("Mobile Data Selected")
    case 4:
        print("Airplane Mode Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Setting")

# Q3
choice = int(input("Enter choice: "))
match choice:
    case 1:
        print("Check Balance Selected")
    case 2:
        print("Withdraw Money Selected")
    case 3:
        print("Deposit Money Selected")
    case 4:
        print("Change PIN Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")

# Q4
signal = input("Enter signal: ").lower().strip()
match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")

# Q5
choice = int(input("Enter choice: "))
match choice:
    case 1:
        print("Opening Profile")
    case 2:
        print("Opening Courses")
    case 3:
        print("Opening Marks")
    case 4:
        print("Opening Attendance")
    case 5:
        print("Logging out")
    case _:
        print("Invalid Choice")

# Q6
category = int(input("Enter category: "))
match category:
    case 1:
        print("Opening Electronics")
    case 2:
        print("Opening Clothing")
    case 3:
        print("Opening Books")
    case 4:
        print("Opening Grocery")
    case 5:
        print("Exiting")
    case _:
        print("Invalid Category")

# Q7
service = int(input("Enter service: "))
match service:
    case 1:
        print("Opening Account Balance")
    case 2:
        print("Opening Mini Statement")
    case 3:
        print("Opening Fund Transfer")
    case 4:
        print("Opening Bill Payment")
    case 5:
        print("Opening Customer Support")
    case _:
        print("Invalid Service")

# Q8
show = int(input("Enter show: "))
match show:
    case 1:
        print("Morning Show Selected")
    case 2:
        print("Afternoon Show Selected")
    case 3:
        print("Evening Show Selected")
    case 4:
        print("Night Show Selected")
    case _:
        print("Invalid Show Choice")

# Q9
weather = input("Enter weather: ").lower().strip()
match weather:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Carry an umbrella")
    case "cloudy":
        print("Weather may change")
    case "snowy":
        print("Wear warm clothes")
    case _:
        print("Unknown Weather")

# Q10
payment = input("Enter payment method: ").lower().strip()
match payment:
    case "upi":
        print("UPI Payment Selected")
    case "card":
        print("Card Payment Selected")
    case "cash":
        print("Cash Payment Selected")
    case "wallet":
        print("Wallet Payment Selected")
    case _:
        print("Invalid Payment Method")

# Q11
ext = input("Enter extension: ").lower().strip()
match ext:
    case "pdf":
        print("Document")
    case "jpg" | "png":
        print("Image")
    case "mp3":
        print("Audio File")
    case "mp4":
        print("Video")
    case _:
        print("Unknown File Type")

# Q12
role = input("Enter role: ").lower().strip()
match role:
    case "admin":
        print("Full Access")
    case "teacher":
        print("Teacher Dashboard")
    case "student":
        print("Student Dashboard")
    case "guest":
        print("Limited Access")
    case _:
        print("Invalid Role")

# Q13
day = int(input("Enter day number: "))
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")

# Q14
priority = int(input("Enter priority number: "))
match priority:
    case 1 | 2:
        print("Normal Priority")
    case 3 | 4:
        print("Urgent Priority")
    case _:
        print("Invalid Priority Number")

# Q15
level = int(input("Enter membership level: "))
match level:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")
    case _:
        print("Invalid Level")

# Q16
user_type = int(input("Enter user type: "))
option = int(input("Enter option: "))
match user_type:
    case 1:
        match option:
            case 1:
                print("Opening Student Courses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case _:
                print("Invalid Option")
    case 2:
        match option:
            case 1:
                print("Opening View Students")
            case 2:
                print("Opening Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid User Type")

# Q17
acc_type = int(input("Enter account type: "))
operation = int(input("Enter operation: "))
match acc_type:
    case 1:
        print("Savings Account")
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")
    case 2:
        print("Current Account")
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")
    case _:
        print("Invalid Account Type")

# Q18
category = int(input("Enter category: "))
product = int(input("Enter product: "))
match category:
    case 1:
        match product:
            case 1:
                print("Mobile Selected")
            case 2:
                print("Laptop Selected")
            case 3:
                print("Headphones Selected")
            case _:
                print("Invalid Product")
    case 2:
        match product:
            case 1:
                print("Shirt Selected")
            case 2:
                print("Jeans Selected")
            case 3:
                print("Shoes Selected")
            case _:
                print("Invalid Product")
    case _:
        print("Invalid Category")

# Q19
category = int(input("Enter category: "))
food = int(input("Enter food: "))
match category:
    case 1:
        match food:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")
            case _:
                print("Invalid Food Option")
    case 2:
        match food:
            case 1:
                print("Chicken Biryani Selected")
            case 2:
                print("Chicken Curry Selected")
            case 3:
                print("Fish Fry Selected")
            case _:
                print("Invalid Food Option")
    case _:
        print("Invalid Category")

# Q20
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator: ").strip()

match op:
    case "+":
        print(f"Result = {num1 + num2}")
    case "-":
        print(f"Result = {num1 - num2}")
    case "*":
        print(f"Result = {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"Result = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid Operator")

# Q21
choice = int(input("Enter choice: "))
temp = float(input("Enter temperature: "))
match choice:
    case 1:
        res = (temp * 9/5) + 32
        print(f"Temperature = {res:.1f} F")
    case 2:
        res = (temp - 32) * 5/9
        print(f"Temperature = {res:.1f} C")
    case _:
        print("Invalid Choice")

# Q22
choice = int(input("Enter choice: "))
val = float(input("Enter value: "))
match choice:
    case 1:
        print(f"{int(val * 1000)} meters")
    case 2:
        print(f"{val / 1000} kilometers")
    case 3:
        print(f"{val * 1000} grams")
    case 4:
        print(f"{val / 1000} kilograms")
    case _:
        print("Invalid Conversion Choice")

# Q23
acc_type = int(input("Enter account type: "))
amount = float(input("Enter amount: "))

match acc_type:
    case 1:
        print("Savings Account")
        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")
    case 2:
        print("Current Account")
        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")
    case _:
        print("Invalid Account Type")

# Q24
choice = int(input("Enter choice: "))
match choice:
    case 1:
        age = int(input("Enter age: "))
        if age >= 18:
            print("You can start the exam")
        else:
            print("You are not eligible to start the exam")
    case 2:
        print("Viewing Result")
    case 3:
        print("Exiting")
    case _:
        print("Invalid Choice")

# Q25
ticket_type = int(input("Enter ticket choice: "))
age = int(input("Enter age: "))

if age < 5:
    print("Free Entry")
else:
    match ticket_type:
        case 1:
            print("Regular Ticket Selected")
        case 2:
            print("Premium Ticket Selected")
        case 3:
            print("VIP Ticket Selected")
        case _:
            print("Invalid Ticket Type")

# Q26
device = int(input("Enter device choice: "))
match device:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid Device")

# Q27
dept = int(input("Enter department choice: "))
match dept:
    case 1:
        print("General Medicine Selected")
    case 2:
        print("Cardiology Selected")
    case 3:
        print("Orthopedics Selected")
    case 4:
        print("Pediatrics Selected")
    case 5:
        print("Emergency Selected")
    case _:
        print("Invalid Department")

# Q28
action = int(input("Enter action choice: "))
match action:
    case 1:
        print("Booking Ticket")
    case 2:
        print("Cancelling Ticket")
    case 3:
        print("Checking PNR")
    case 4:
        print("Viewing Train Schedule")
    case 5:
        print("Exit")
    case _:
        print("Invalid Action")

# Q29
choice = int(input("Enter library option: "))
match choice:
    case 1:
        print("Searching Book")
    case 2:
        print("Issuing Book")
    case 3:
        print("Returning Book")
    case 4:
        print("Viewing Issued Books")
    case 5:
        print("Exit")
    case _:
        print("Invalid Option")

# Q30
status = input("Enter status: ").lower().strip()
match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order is confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order was cancelled")
    case _:
        print("Invalid Order Status")

# Q31
b_type = int(input("Enter banking type: "))
opt = int(input("Enter option: "))
match b_type:
    case 1:
        match opt:
            case 1:
                print("Personal Balance Selected")
            case 2:
                print("Personal Transfer Selected")
            case 3:
                print("Personal Loan Selected")
            case _:
                print("Invalid Option")
    case 2:
        match opt:
            case 1:
                print("Business Balance Selected")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Banking Type")

# Q32
role = int(input("Enter role choice: "))
opt = int(input("Enter option choice: "))
match role:
    case 1:
        match opt:
            case 1:
                print("Student Marks")
            case 2:
                print("Student Attendance")
            case 3:
                print("Student Homework")
            case _:
                print("Invalid Option")
    case 2:
        match opt:
            case 1:
                print("Teacher Enter Marks")
            case 2:
                print("Teacher Attendance")
            case 3:
                print("Teacher Assign Homework")
            case _:
                print("Invalid Option")
    case 3:
        match opt:
            case 1:
                print("Parent Child Marks")
            case 2:
                print("Parent Child Attendance")
            case 3:
                print("Parent Contact Teacher")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Role")

# Q33
transport = int(input("Enter transport: "))
opt = int(input("Enter class/option: "))
match transport:
    case 1:
        match opt:
            case 1:
                print("Flight - Economy Selected")
            case 2:
                print("Flight - Business Selected")
            case _:
                print("Invalid Class")
    case 2:
        match opt:
            case 1:
                print("Train - Sleeper Selected")
            case 2:
                print("Train - AC Selected")
            case _:
                print("Invalid Class")
    case 3:
        match opt:
            case 1:
                print("Bus - Ordinary Selected")
            case 2:
                print("Bus - Volvo Selected")
            case _:
                print("Invalid Class")
    case _:
        print("Invalid Transport Method")

# Q34
choice = int(input("Enter menu choice: "))
match choice:
    case 1:
        print("Starting Game...")
    case 2:
        print("Loading Game...")
    case 3:
        setting_opt = int(input("Enter settings option: "))
        match setting_opt:
            case 1:
                print("Sound Settings Opened")
            case 2:
                print("Graphics Settings Opened")
            case 3:
                print("Controls Settings Opened")
            case _:
                print("Invalid Settings Option")
    case 4:
        print("Exiting...")
    case _:
        print("Invalid Choice")

# Q35
cat = int(input("Enter category choice: "))
item = int(input("Enter item choice: "))
match cat:
    case 1:
        match item:
            case 1:
                print("Soup Selected")
            case 2:
                print("Spring Roll Selected")
            case 3:
                print("Garlic Bread Selected")
            case _:
                print("Invalid Starter")
    case 2:
        match item:
            case 1:
                print("Pizza Selected")
            case 2:
                print("Pasta Selected")
            case 3:
                print("Biryani Selected")
            case _:
                print("Invalid Main Course")
    case 3:
        match item:
            case 1:
                print("Ice Cream Selected")
            case 2:
                print("Cake Selected")
            case 3:
                print("Gulab Jamun Selected")
            case _:
                print("Invalid Dessert")
    case 4:
        match item:
            case 1:
                print("Coffee Selected")
            case 2:
                print("Tea Selected")
            case 3:
                print("Juice Selected")
            case _:
                print("Invalid Drink")
    case _:
        print("Invalid Category")

# Q36
payment_type = int(input("Enter payment type: "))
opt = int(input("Enter option: "))
match payment_type:
    case 1:
        match opt:
            case 1:
                print("Scanning QR Code...")
            case 2:
                print("Enter UPI ID Selected")
            case _:
                print("Invalid UPI Option")
    case 2:
        match opt:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid Card Option")
    case 3:
        match opt:
            case 1:
                print("Add Money Selected")
            case 2:
                print("Pay Using Wallet Selected")
            case _:
                print("Invalid Wallet Option")
    case _:
        print("Invalid Payment Type")

# Q37
subject = int(input("Enter domain choice: "))
topic = int(input("Enter course choice: "))
match subject:
    case 1:
        match topic:
            case 1:
                print("Python Course Selected")
            case 2:
                print("Java Course Selected")
            case 3:
                print("C++ Course Selected")
            case _:
                print("Invalid Course")
    case 2:
        match topic:
            case 1:
                print("Algebra Course Selected")
            case 2:
                print("Calculus Course Selected")
            case 3:
                print("Statistics Course Selected")
            case _:
                print("Invalid Course")
    case 3:
        match topic:
            case 1:
                print("English Course Selected")
            case 2:
                print("Presentation Course Selected")
            case 3:
                print("Interview Skills Course Selected")
            case _:
                print("Invalid Course")
    case _:
        print("Invalid Subject")

# Q38
main_opt = int(input("Enter main dashboard option: "))
sub_opt = int(input("Enter specific control: "))
match main_opt:
    case 1:
        match sub_opt:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid Engine Option")
    case 2:
        match sub_opt:
            case 1:
                print("Headlights Toggled")
            case 2:
                print("Indicators Toggled")
            case 3:
                print("Hazard Lights Toggled")
            case _:
                print("Invalid Lights Option")
    case 3:
        match sub_opt:
            case 1:
                print("Playing Music")
            case 2:
                print("Music Paused")
            case 3:
                print("Next Track")
            case 4:
                print("Previous Track")
            case _:
                print("Invalid Music Option")
    case 4:
        match sub_opt:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid Navigation Option")
    case _:
        print("Invalid Dashboard Option")

# Q39
user_type = int(input("Enter role: "))
opt = int(input("Enter option: "))
match user_type:
    case 1:
        match opt:
            case 1:
                print("Opening Employee Profile")
            case 2:
                days = int(input("Enter leave days: "))
                if days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")
            case 3:
                print("Opening View Salary")
            case _:
                print("Invalid Employee Option")
    case 2:
        match opt:
            case 1:
                print("Opening View Team")
            case 2:
                print("Opening Approve Leave")
            case 3:
                print("Opening View Reports")
            case _:
                print("Invalid Manager Option")
    case _:
        print("Invalid Role")

# Q40
role = int(input("Enter role: "))
opt = int(input("Enter option: "))
match role:
    case 1:
        match opt:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Option")
    case 2:
        match opt:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Opening Teacher Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Option")
    case 3:
        match opt:
            case 1:
                print("Opening Admin Fees")
            case 2:
                print("Opening Admin Admissions")
            case 3:
                print("Opening Admin Notices")
            case 4:
                print("Opening Admin Departments")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Role")
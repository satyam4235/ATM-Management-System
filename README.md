# 🏦 ATM Management System (Python Project)

## 📌 Project Overview
This is a Python-based **ATM Management System** built using **Object-Oriented Programming (OOP)** principles.  
The project simulates an ATM machine where users can:
- Create a PIN  
- Deposit money  
- Withdraw funds  
- Check balance  
- Change PIN  
- View transaction history with timestamps  

The system includes **error handling, input validation, and transaction tracking**, making it a great example of Python OOP and real-world application.

---

## 🚀 Features
- 🔑 **Create PIN** → Secure user authentication with 4-digit PIN setup  
- 💰 **Deposit Money** → Add money with transaction logging  
- 💸 **Withdraw Money** → Withdraw funds with balance validation  
- 📊 **Check Balance** → View current account balance  
- 🔄 **Change PIN** → Update PIN securely with confirmation  
- 📜 **Transaction History** → View deposits & withdrawals with date & time  
- ⚡ **Error Handling** → Handles invalid inputs, incorrect PINs, and insufficient balance  

---

## 🛠️ Tech Stack
- **Language**: Python 3  
- **Modules Used**:  
  - `datetime` → For transaction timestamps  

---

## 📂 Project Structure
ATM-Management-System/
│── atm.py # Main Python file containing the ATM class
│── README.md # Project documentation

---

## 🖥️ How to Run
1. Clone this repository:  
   git clone https://github.com/your-username/ATM-Management-System.git
Navigate to the project folder:

cd ATM-Management-System
Run the program:

python atm.py
📸 Sample Output

Enter a four digit pin: 1234
Renter your pin: 1234
Your pin is created successfully!

Enter your pin no: 1234
Enter amount to deposit: 5000
Amount deposited successfully. your account balance is: 5000.0

-------Transaction History---------
2025-09-19  23:10:45 | Deposit   | Rs.5000.0
-----------------------------------
🎯 Learning Outcomes
Understanding OOP concepts in Python

Practical use of classes, objects, methods, and attributes

User authentication with PINs

Using datetime for logging transactions

Building a banking simulation

📌 Future Enhancements
Add multiple users with account numbers

Connect to a database (SQLite / MySQL) for persistent storage

Build a GUI version using Tkinter or PyQt

Implement card number validation & security features

📜 License
This project is licensed under the MIT License – you are free to use, modify, and distribute it.
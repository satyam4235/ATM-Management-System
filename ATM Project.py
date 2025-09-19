#!/usr/bin/env python
# coding: utf-8

# In[8]:


import datetime

class Atm:
    def __init__(self,name):
        self.name = name
        self.pin = self.create_Pin()
        self.balance = 0
        self.Transaction_history = []


    def create_Pin(self):
        pin = int(input("Enter a four digit pin: "))
        check = int(input("Renter your pin: "))
        while True:
            if pin == check:
                print("Your pin is created successfully!")
                return pin
            else:
                print("Your pin don't match! please try again!")
                pin = int(input("Enter a four digit pin: "))
                check = int(input("Renter your pin: "))

    def deposit(self):
        check = int(input("Enter your pin no : "))
        if check == self.pin:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"Amount deposited successfully. your account balance is: {self.balance}")
                self.Transaction_history.append({
                    "type":"Deposit",
                    "amount": amount,
                    "date_time":datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")})
            else:
                print("Invalid amount. please enter a positive number.")
        else:
            print("Incorrect pin!")

    def check_balance(self):
        entered_pin = int(input("Enter your pin no : "))
        if entered_pin == self.pin:
            print(f"Your Account balance is :{self.balance}")
        else:
            print("Incorrect pin!")

    def withdraw(self):
        cp = int(input("Enter your pin no : "))
        if cp == self.pin:
            amount = float(input("Enter amount to Withdraw: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print(f"Amount withdrawn successfully. your account balance is: {self.balance}")
                self.Transaction_history.append({
                    "type":"Withdraw",
                    "amount": amount,
                    "date_time":datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")})
            else:
                print("Insufficient Balance!")

    def change_pin(self):
        current_pin = int(input("Enter your current pin: "))
        if current_pin == self.pin:
            new_pin = int(input("Enter a new four digit pin: "))
            confirm_pin = int(input("Re-enter your new pin: "))
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("Your pin has been changed successfully.")
            else:
                print("New pins do not match!")
        else:
            print("Incorrect current pin!")

    def show_history(self):
        print("\n-------Transaction History---------")
        if not self.Transaction_history:
            print("No Transaction history")
        else:
            for t in self.Transaction_history:
                print(f"{t["date_time"]} | {t["type"]}    | Rs.{t["amount"]}")
        print("-----------------------------------------")




# In[2]:


RossGeller = Atm("Ross Geller")


# In[3]:


RossGeller.deposit()


# In[4]:


RossGeller.check_balance()


# In[5]:


RossGeller.withdraw()


# In[6]:


RossGeller.change_pin()


# In[10]:


RossGeller.show_history()


# In[ ]:





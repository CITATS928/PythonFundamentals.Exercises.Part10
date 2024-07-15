import pickle
import os
from persistent_small_town_teller import PersistenceUtils


#Class person with ID, FirstName and LastName
class Person:
    def __init__(self, id, First_Name, Last_Name):
        # Initialize a new Person instance
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.id = id
        

#Class for a bank account with Number, Type, Owner and balance
class Account:
    def __init__(self, Number,Type,Owner,Balance=0.0):
        # Initialize a new Account instance
        self.Number = Number
        self.Type = Type
        self.Owner = Owner
        self.Balance = Balance
        





#A bank with customers and accounts
class Bank:
    def __init__(self):
        # Initialize a new Bank instance
        # Dictionary to store customers with customer ID as the key
        self.customers = {}
        # Dictionary to store accounts with account number as the key
        self.accounts = {}

    #add a customer to a bank
    def Adding_Customer(self,person):
        # Check if the customer is already in the system
        if person.id in self.customers:
            return "already in the system"
        # Add the customer to the customers dictionary
        self.customers[person.id]=person


    #add a account to a bank
    def Adding_Account(self,account):
        # Check if the account is already in the system
        if account.Number in self.accounts:
            return "already in system"
        # Add the account to the accounts dictionary
        self.accounts[account.Number]=account


    #remove an account from the bank
    def Removing_Account(self,number):
        # Check if the account exists in the system
        if number not in self.accounts:
            return "not in the system"
        # Remove the account from the accounts dictionary
        del self.accounts[number]


    # Method to deposit money into an account
    def Depositing_Money(self,account_number, money):
        self.accounts[account_number].Balance+=money


    # Method to withdraw money from an account
    def Withdrawing_Money(self,account_number,money):
        if self.accounts[account_number].Balance >=money:
            self.accounts[account_number].Balance-=money
        else:
            return "not enough money"
        

    # Method to inquire the balance of an account
    def Balance_Inquiry(self,account_number):
        return self.accounts[account_number].Balance
        

    # Method to save the bank data to a file
    def save_data(self,file_name = 'bank_data.pickle'):
        # Create a dictionary with the current state of customers and accounts
        data = {"customer":self.customers,
                "account":self.accounts}
        # Use the PersistenceUtils class to write this data to a file
        PersistenceUtils.write_pickle(file_name,data)
        


    # Method to load the bank data from a file
    def load_data(self, file_name ='bank_data.pickle'):
        # Use the PersistenceUtils class to read data from a file
        data = PersistenceUtils.load_pickle(file_name)
        # Update the current state of customers and accounts with the loaded data
        self.customers = data["customer"]
        self.accounts = data["account"]
        
    
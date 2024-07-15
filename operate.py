from small_town_teller import Person,Account,Bank

zc_bank = Bank()
bob = Person(1,"Bob","Smith")
zc_bank.Adding_Customer(bob)
bob_saving = Account(1001,"saving",bob)
zc_bank.Adding_Account(bob_saving)
print(zc_bank.Balance_Inquiry(1001))
zc_bank.Depositing_Money(1001,5000.50)
print(zc_bank.Balance_Inquiry(1001))
zc_bank.Withdrawing_Money(1001,5.5)
print(zc_bank.Balance_Inquiry(1001))
zc_bank.save_data() 

zc_bank.load_data()
print(zc_bank.customers)
print(zc_bank.accounts)
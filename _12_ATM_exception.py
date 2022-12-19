### Program to manage ATM operations Deposit, Withdrawl and mini-statement
from _11_custom_exception import InvalidPINError,InvalidAmountError,InvalidAmountError1,InvalidAmountError2
class ATM_PIN:
    pin_file=open("atm_pin","w")
    pin_file.write("1234")
    pin_file.close()
    pin_file=open("atm_pin","r")
    data=pin_file.read()

class atm_operation(ATM_PIN):
    def atm(self,atm_pin):
        self.atm_pin=atm_pin
        pin_file1=open("atm_pin1","w")
        pin_file1.write(str(atm_pin))
        pin_file1.close()
        pin_file1=open("atm_pin1","r")
        data1=pin_file1.read()
        if self.data==data1:
            pass
        else:
            raise InvalidPINError()
    def atm_choice(self,choice,balance=10000):
        self.choice=choice
        if choice==1:
            dep_amount=int(input("Enter the amount to be deposited: "))
            if dep_amount>25000:
                raise InvalidAmountError
            if dep_amount%500!=0:
                raise InvalidAmountError1
            else:
                balance+=dep_amount
                print("Successfully deposited. \nYour current Balance is ", balance)
        if choice==2:
            wtdrl_amt=int(input("Enter the amount to be withdrawn: "))
            if wtdrl_amt<=25000:
                balance-=wtdrl_amt
                print("Your current balance amount: ", balance)
            else:
                raise InvalidAmountError2
        if choice==3:
            print("Your current balance is ", balance)

obj=atm_operation()
try:
    atm_pin=int(input("Enter your 4-digit ATM PIN Number: "))
    obj.atm(atm_pin)
except InvalidPINError as ex:
    print(ex)
else:
    print("The Choices are as follows.\n 1.Deposit\n 2.Withdrawl\n 3.View Mini-statement\n")
    try:
        choice=int(input("Enter your choice:  "))
        obj.atm_choice(choice)
    except InvalidAmountError as ex:
        print(ex)
    except InvalidAmountError1 as ex:
        print(ex)
    except InvalidAmountError2 as ex:
        print(ex)


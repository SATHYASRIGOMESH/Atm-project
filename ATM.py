
import datetime
today=datetime.datetime.now()
print(today)

print("*****WELCOME TO STATE BANK OF INDIA****")
print("Please insert your card")
print("what do you want to do")
print("***widthdraw cash" )
print("***deposite cash")
print("****Balance enquiry")
print("***Exit")

def password(number):
    print("your bank password is:",number)

password(1234)

PIN=int(input("Enter your 4 digit pin:"))
 
def account(balance):
    print("your current balance is:",balance)
account(10000)

print("1.Tamil")
print("2.English")
print("3.Hindhi")

language=int(input("Enter your choise:"))

if language==1:  
     print("you are select Tamil")

elif language==2:

 print("your language English")

elif language==3:

 print("your language Hindhi")

else:
    print("Incorrect choice")


if password==PIN:

        print("1.widthdraw cash")
        print("2.deposite")
        print("3.Balance enquiry")
        print("4.Exit")
        
try:
       
 Card_Holder=int(input("Enter your option:"))

except:

    print("Please Enter Valid Option")

    user="Card_Holder"

if Card_Holder==1:

       print(input("enter your amount:"))

       print("widthdraw is successfully")
    


elif Card_Holder==2:
     print(input("enter your deposite amount:"))

     print("your deposite is successfully")


elif Card_Holder==3:

    print("check the balance")

    print("your balance enquiry process is successfully")

elif Card_Holder==4:

    print("EXIT the process")

else:

    print("please check your account details")


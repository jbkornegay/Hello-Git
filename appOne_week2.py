import datetime as dt
import random
now = dt.datetime.now()
dateTime = now.strftime("%B %d, %Y  %I:%M %p")
balance = 0
database = {1234567890: ['Wonder', 'Woman', 'wwoman@dccomics.com', 'wwpass']}

def init():
    print(dateTime)
    print('Welcome to C & S Savings Bank')
    haveAccount = int(input('Do you have an account with us?: 1 (yes) 2 (no) \n'))
   
    if haveAccount == 1:
       login()
    elif haveAccount == 2:
       register()
    else:
        print('You have selected an invalid option.\n\n')
        init()

def login():
    print('Login to your account.')
    
    accountNumberFromUser = int(input('Please enter your account number: \n'))
    password = input('Please enter your password: \n')

    for accountNumber,userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                print('\nWelcome %s %s\n' % (userDetails[0], userDetails[1] ) )
                bankOperations()           
    else:
        print('Invalid account number or password.\n')
        login()

def register():
    print('*****Please register for your new account.*****')
    email = input('Please enter your email address: \n')
    first_name = input('Please enter your first name: \n')
    last_name = input('Please enter your last name: \n')
    password = input('Please create a password for your account: \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]
    
    print('\nYour Account has been created')
    print('Your Account Number is: ', accountNumber, '\n')

    login()

def generateAccountNumber():

    return random.randrange(1111111111,9999999999)

def bankOperations():
    print('Please select from the following options: ')
    print('1.  Withdrawal')
    print('2.  Cash Deposit')
    print('3.  Complaint')
    print('4.  Exit')
    selectedOption = int(input('Please enter your selection: \n'))

    if selectedOption == 1:
        withdrawalOperation()
            
    elif selectedOption == 2:
        depositOperation()
    
    elif selectedOption == 3:
        complaintOperation()
    
    elif selectedOption == 4:
        print('Have a nice day!')
        exit()

    else:
        print('Invalid Option selected, please try again.')
        bankOperations()
          
def withdrawalOperation():
    
    withdrawal = int(input('How much would you like to withdraw? \n'))
    global balance
    balance -= withdrawal
    print('\nYour current balance is: ', balance)
    print ('Please take your cash.\n')
    bankOperations()
    
def depositOperation():
    deposit = int(input("How much would you like to deposit? \n"))
    global balance
    balance += deposit
    print('\nYour current balance is: ', balance, '\n')
    bankOperations()    

def complaintOperation():
    input('What issue would you like to report? \n')
    print('\nThank you for contacting us.\n')
    bankOperations()


###Beginning of Program

init()

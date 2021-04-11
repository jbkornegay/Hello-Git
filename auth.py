#register
# - first name, last name, password, email
# - generate account


#login
# - accoount number and password


#bank operations

#Initializing the system
import random

database ={} #dictionary

def init():

    print('Welcome to C & S Savings Bank')

    haveAccount = int(input('Do you have an account with us?: 1 (yes) 2 (no) \n'))
   
    if haveAccount == 1:
       login()
    elif haveAccount == 2:
       register()
    else:
        print('You have selected an invalid option.')
        init()


def login():
    print('Login to your account.')
    
    accountNumberFromUser = int(input('Please enter your account number: \n'))
    password = input('Please enter your password: \n')

    for accountNumber,userDetails in database.items():
         if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                 bankOperation(userDetails)

    print('Invalid account or password')
    login()
    
    
def register():
    print('*****Please register for your new account.*****')
    email = input('Please enter your email address: \n')
    first_name = input('Please enter your first name: \n')
    last_name = input('Please enter your last name: \n')
    password = input('Please create a password for your account: \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]
    
    print('Your Account has been created')
    print('Your Account Number is: ', accountNumber)

    login()




def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1] ) )
    selectedOption = int(input('What would yu like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))

    if selectedOption == 1:
        depositOperation()
    elif selectedOption == 2:
        withdrawalOperation()
    elif selectedOption == 3:
        logout()
    elif selectedOption == 4:
        exit()
    else:
        print('Invalid option selected')
        bankOperation(user)

def withdrawalOperation():
    print('Withdrawal')

def depositOperation():
    print('Deposit Operations')

def generateAccountNumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()



#######Actual Banking System############

init() 









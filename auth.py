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

    isValidOptionSelected = False
    print('Welcome to C & S Savings Bank')

    while isValidOptionSelected == False:

        haveAccount = int(input('Do you have an account with us?: 1 (yes) 2 (no) \n'))
   
        if haveAccount == 1:
            isValidOptionSelected = True
            login()
        elif haveAccount == 2:
            isValidOptionSelected = True
            register()
        else:
            print('You have selected an invalid option.')


def login():
    print('Login to your account.')
    bankOperation()
    
def register():
    print('*****Please register for your new account.*****')
    email = input('Please enter your email address: \n')
    first_name = input('Please enter your first name: \n')
    last_name = input('Please enter your last name: \n')
    password = input('Please create a password for yourself: \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]
    
    print('Your Account has been created')
    login()



def bankOperation():
    print('some operations')

def generateAccountNumber():

    return random.randrange(1111111111,9999999999)



#######Actual Banking System############

init() 









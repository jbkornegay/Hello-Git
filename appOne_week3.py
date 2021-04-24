import datetime as dt
import random
import auth_files
import validation
import database
from getpass import getpass

now = dt.datetime.now()
dateTime = now.strftime("%B %d, %Y  %I:%M %p")


def init():
    print(dateTime)
    print('Welcome to C & S Savings Bank')
    have_account = int(input('Do you have an account with us?: 1 (yes) 2 (no) \n'))

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print('You have selected an invalid option.\n\n')
        init()


def login():
    print('Login to your account.')

    account_number_from_user = int(input('Please enter your account number: \n'))

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass('Please enter your password: \n')
        user = database.authenticated_user(account_number_from_user, password)

        if user:
            auth_files.create_file(account_number_from_user)
            print("Welcome %s %s " % (user[0], user[1]))
            bank_operations(account_number_from_user)

        else:
            print("Invalid account or password")
            login()

    else:
        print('Account Number Invalid:  check that you have 10 digits and only integers.')
        init()


def register():
    print('*****Please register for your new account*****')
    email = input('Please enter your email address: \n')
    first_name = input('Please enter your first name: \n')
    last_name = input('Please enter your last name: \n')
    password = getpass('Please create a password for your account: \n')

    account_number = generate_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print('\nYour Account has been created')
        print('Your Account Number is:  %d' % account_number, '\n')

        login()

    else:
        print("Something went wrong, please try again.")
        register()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def bank_operations(user_account_number):

    print('Please select from the following options: ')
    print('1.  Withdrawal')
    print('2.  Cash Deposit')
    print('3.  Register a complaint')
    print('4.  Logout')
    selected_option = int(input('Please enter your selection: \n'))

    if selected_option == 1:
        withdrawal_operation(user_account_number)

    elif selected_option == 2:
        deposit_operation(user_account_number)

    elif selected_option == 3:
        complaint_operation(user_account_number)

    elif selected_option == 4:
        logout(user_account_number)

    else:
        print('Invalid Option selected, please try again.')
        bank_operations(user_account_number)


def withdrawal_operation(user_account_number):
    withdrawal = int(input('How much would you like to withdraw? \n'))
    record_path = "data/user_record/"
    f = open(record_path + str(user_account_number) + ".txt", )
    user_record = f.readline()
    user_list = user_record.split(",")

    if int(user_list[4]) >= withdrawal:

        current_balance = int(user_list[4]) - withdrawal
        f.close()
        user_list[4] = str(current_balance)
        user_string = ",".join(user_list)
        f = open(record_path + str(user_account_number) + ".txt", "w")
        f.write(user_string)
        f.close()
        print('\nYour current balance is: ', current_balance)
        print('Please take your cash.\n')
        bank_operations(user_account_number)

    else:
        print("The withdrawal amount exceeds your current balance.")
        bank_operations(user_account_number)


def deposit_operation(user_account_number):
    record_path = "data/user_record/"
    deposit = int(input("How much would you like to deposit? \n"))
    f = open(record_path + str(user_account_number) + ".txt",)
    user_record = f.readline()
    user_list = user_record.split(",")
    current_balance = int(user_list[4]) + deposit
    f.close()
    user_list[4] = str(current_balance)
    user_string = ",".join(user_list)
    f = open(record_path + str(user_account_number) + ".txt", "w")
    f.write(user_string)
    f.close()
    print('\nYour current balance is: ', current_balance, '\n')
    bank_operations(user_account_number)


def complaint_operation(user_account_number):
    input('What issue would you like to report? \n')
    print('\nThank you for contacting us.\n')
    bank_operations(user_account_number)


def logout(user_account_number):
    auth_files.delete_file(user_account_number)
    print("Have a nice day!")
    exit()


init()

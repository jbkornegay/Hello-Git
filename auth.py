# register
# - first name, last name, password, email
# - generate account


# login
# - account number and password


# bank operations

# Initializing the system
import random
import validation
import database
from getpass import getpass


def init():
    print('Welcome to C & S Savings Bank')

    have_account = int(input('Do you have an account with us?: 1 (yes) 2 (no) \n'))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print('You have selected an invalid option.')
        init()


def login():
    print('Login to your account.')

    account_number_from_user = input('Please enter your account number: \n')

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass('Please enter your password: \n')

        user = database.authenticated_user(account_number_from_user, password);

        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid:  check that you have 10 digits and only integers.")
        init()


def register():
    print('*****Please register for your new account.*****')

    email = input('Please enter your email address: \n')
    first_name = input('Please enter your first name: \n')
    last_name = input('Please enter your last name: \n')
    password = getpass('Please create a password for your account: \n')

    account_number = generate_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print('Your Account has been created')
        print(" == ==== ====== ===== ===")
        print("Your Account Number is:  %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong. Please try again.")
        register()


def bank_operation(user):
    print('Welcome %s %s' % (user[0], user[1]))

    selected_option = int(input('What would yu like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print('Invalid option selected')
        bank_operation(user)


def withdrawal_operation():
    print('Withdrawal')
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance


def deposit_operation():
    print('Deposit Operations')
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()


init()

# create a file when user logs in
# delete file when user logs out

import os
user_file_path = "data/auth_session/"


def create_file(user_account_number):

    try:

        f = open(user_file_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:
        print("User is already logged in.")

    else:
        f.close()



def delete_file(user_account_number):
    if os.path.exists(user_file_path + str(user_account_number) + ".txt"):
        os.remove(user_file_path + str(user_account_number) + ".txt")
    else:
        print("The file does not exist")



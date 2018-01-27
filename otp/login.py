import json
import pyotp, qrcode
import os
import logging


def offerotp(username, password):
    print("Would you like to use OTP instead of password?(Y/N)")
    choice= input();
    if choice == 'Y' or choice == 'y':
        print("Please scan below QR Code and enter the otp generated")
        
        totp = pyotp.totp.TOTP(password)
        url = totp.provisioning_uri(username, issuer_name="Secure App")
        img=qrcode.make(url)
        img.show()
        code = input()
        return totp.verify(code, valid_window=1)
    else:
        return False
            

def login(create_flag = False):
    print("Username: ")
    username = input ()

    print("Password: ")
    password = input ()
    
    success = False

    user = read_user_file(username)
        
    logger.debug(user)

    if user:
        if user.get("otp_enabled"):
            logger.info("User is OTP enabled")
            totp = pyotp.totp.TOTP(user.get('password'))

            if totp.verify(otp, valid_window=1):
                logger.info ("Password accepted")
            else:
                logger.info ("Password not accepted")
        else:
            if password == user.get('password'):
                logger.info ("Password accepted")
                if create_flag and\
                    not(user.get('otp_enabled')):
                    if offerotp(username, password):
                        user['otp_enabled'] = True
                        logger.info("User enabled with OTP")
                    else:
                        user['otp_enabled'] = False
            else:
                logger.info ("Password not accepted")
    elif create_flag:
        print ("User %s not found. Enter password again to create"% username)
        
        if password == input ():
            user= {}
            user['name'] = username
            user['password'] = password
            logger.info("User password created")
            if offerotp(username, user['password']):
                user['otp_enabled'] = True
            else:
                user['otp_enabled'] = False
            logger.info("User enabled with OTP: {}".format(
                user['otp_enabled'] ))
        else:
            logger.info("Passwords didnt match. Exiting..")
    else:
        logger.info("Invalid username or password entered")
    return user

def run_application(args):
    from subprocess import run
    run(args)
    return

def read_user_file(filename):
    filename = PATH + filename
    if os.path.isfile(filename):
        with open(filename) as infile:
            user_details= json.load(infile)
    else:
        user_details = None
    return user_details

def def_update_user(user):
    filename = PATH + user['name']
    with open(filename, 'w') as outfile:
            json.dump(user, outfile)
    

#------------------------------------------------
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

PATH = './'
#------------------------------------------------

if __name__ == "__main__":
    
    try:
        user = login(False)
        if user:
            logger.debug("Updating User")
            def_update_user(user)
            logger.info("Login successfull. Now running application")
            import sys
            if(len(sys.argv) > 1):
                run_application(str(sys.argv[1:]))
            else:
                run_application("python bit.py")        
    
    
    except Exception as err:
        logger.error(err)
        logger.info("Error, lets start again")

        

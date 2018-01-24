import json
import pyotp, qrcode
import os

def offerotp(username, password, otp_list):
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
    return
            

def login():
    print("Username: ")
    username = input ()

    if username in password_list:
        if username in otp_list:
            print("OTP: ")
            otp = input()
            password = password_list[username]
            totp = pyotp.totp.TOTP(password)

            if totp.verify(otp, valid_window=1):
                print ("Password accepted")
            else:
                print ("Password not accepted")
        else:
            print("Password: ")
            password = input ()
            if password == password_list[username] :
                print ("Password accepted")
                if offerotp(username, password, otp_list):
                    otp_list[username]="true"
                    print ("User enabled with OTP")
            else:
                print ("Password not accepted")
    else:
        print ("User %s not found. Enter password to create"% username)
        password = input ()
        password_list[username]=password
        

password_list ={}
otp_list={}


filename = 'passwords.txt'
if os.path.isfile(filename):
    with open(filename) as infile:
        password_list = json.load(infile)

filename = 'otp.txt'
if os.path.isfile(filename):
    with open(filename) as infile:
        otp_list = json.load(infile)
try:
    login()
    from bit import getpercentfin
    print("Bitcoin Client is %s percent synchronised with blockchain...."% getpercentfin())
    
except Exception:
    print("Error, lets start again")

with open('passwords.txt', 'w') as outfile:
        json.dump(password_list,outfile )

with open('otp.txt', 'w') as outfile:
        json.dump(otp_list,outfile )        
    

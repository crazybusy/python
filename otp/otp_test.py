import pyotp, qrcode, time

totp = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP')

url = totp.provisioning_uri("alice@google.com", issuer_name="Secure App")

img=qrcode.make(url)



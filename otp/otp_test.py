import pyotp, qrcode, time

totp = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP')

url = totp.provisioning_uri("alice@google.com", issuer_name="Secure App")

qr = qrcode.QRCode()
qr.add_data(url)
qr.make()

qrcode.QRCode.print_ascii(qr)

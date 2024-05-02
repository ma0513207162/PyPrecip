import pyotp

key = 'J23YJ5BS2BJOS6ESD4KD6JM436L5UMWS'
totp = pyotp.TOTP(key)
print(totp.now()) 


import math,random

def generateOTP():
    digits='0123456789'
    OTP=''
    for i in range(4):
        OTP+=digits[random.randint(0,9)]
    return OTP
if __name__=="__main__":
    print("Your OTP is: ",generateOTP())

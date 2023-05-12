import random
import time

char = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP\{\}|ASDFGHJKL:\"ZXCVBNM<>?"
# 길이는 96

def ResetPassword():
    password = ""
    for idx in range(10):
        password += char[random.randint(0,len(char)-1)]
    print(password)
    return password

def CreatePassword(timer : int):
    start_time = time.time()
    while time.time() - start_time < timer:
        password = ResetPassword()
        time.sleep(random.uniform(0,.1))
        if time.time() - start_time > timer:
            print("랜덤 패스워드 생성 : ",password)
            return password
        
def Comparison_password(password : str):
    randompassowrd = ResetPassword()
    while randompassowrd != password:
        randompassowrd = ResetPassword()
        if randompassowrd != password:
            # print("같지 않음",randompassowrd)
            pass
        else:
            print("찾음 !!")
            print("찾는 패스워드 : ", password)
            print("찾은 패스워드 : ", randompassowrd)

password = CreatePassword(5)
Comparison_password(password)

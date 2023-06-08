import random
import string
import time
import itertools

class Password:
    def __init__(self):        
        self.password = ""
        self.ord_list = []
        
    def create(self, size : int, chars : str = string.ascii_letters + string.digits + string.punctuation):
        self.ord_list = []
        self.password = [random.choice(chars) for _ in range(size)]
        self.ord_list_update()
        self.password = ''.join(self.password)

    def ord_list_update(self):
        for idx in self.password:
            self.ord_list.append(ord(idx))

    def select_create(self, select : list):
        # 33 ~ 64
        # 65 ~ 96
        # 97 ~ 126
        self.ord_list = []
        self.password = []

        for idx in select:
            self.password.append(chr(idx))

        self.password = ''.join(self.password)
        self.ord_list_update()
    
    def show(self):
        print(f"ord_list : {self.ord_list}")
        print(f"password : {self.password}")
        
    def __del__(self):
        pass

# print("ascii_letters")
# for idx in string.ascii_letters:
#     print(f"{idx} : {ord(idx)}")

# print("digits")
# for idx in string.digits:
#     print(f"{idx} : {ord(idx)}")

# print("punctuation")
# for idx in string.punctuation:
#     print(f"{idx} : {ord(idx)}")

# string.ascii_letters + string.digits + string.punctuation 33 ~ 126


# print("")
temp = Password()
# temp.select_create([65,66])
# temp.show()

size = 4

for tem in itertools.product(range(33,127), repeat=size):
    temp.select_create(tem)
    print(temp.show())

# for x in range(33,127):
#     for x_2 in range(33, 127):
#         for x_3 in range(33, 127):
#             for x_4 in range(33, 127):
#                 temp[0] = x
#                 temp[1] = x_2
#                 temp[2] = x_3
#                 temp[3] = x_4
#                 print(temp)


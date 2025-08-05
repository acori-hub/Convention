import sys
import random
import os
import math

# TODO: 리팩토링 필요
def calculate_stuff(x,y):
   if x>0:
  result = x*3.14159  # 원의 넓이 계산
   else:
        result=y/2.718281828

   return result

class userManager:
    def __init__(self):
        self.temp = []
        
    def doSomething(self, data):
        # 사용자 추가
        if len(data) > 0:
            self.temp.append(data)
        
        else:
            print("Invalid data")
            
    def getData(self):
        return self.temp

def main():
    um = userManager()
    user_input = input("Enter data: ")
    um.doSomething(user_input)
    print(um.getData())

if __name__ == "__main__":
    main()

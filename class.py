class Cal:
    #__init__ 메모리에 올라오는 즉시 실행됨 
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def add(self):
        return self.a + self.b 
    
    def sub(self):
        return self.a - self.b 
    
    def mul(self):
        return self.a * self.b 
    
    def div(self):
        return self.a / self.b 
    

cal1 = Cal(1,2)

print(cal1.a) # cal1 뒤에 . 을 붙히면 메모리에 접근 할수 있게 됨 
print(cal1.b)
print(cal1.add())


####################################################################

#클래스 변수 : 인스턴스들이 공유하는 변수
class Robot:
    population = 0
    # 생성자 함수 
    def __init__(self, name, code):
        self.name = name # 인스턴스 변수 
        self.code = code   # 인스턴스 변수 
        Robot.population+=1
    #인스턴스 매서드     
    def say_hi(self):
        print("hi",self.name)
    
    #인스턴스 매서드 
    def cal_add(self,a,b):
        return a+b
    
    #인스턴스 매서드             
    def die(self):
        print({self.name} ,"is being destroyed!")
        Robot.population -=1
        if Robot.population ==0:
            print ( {self.name}"is last one")
        else:
            print("There are still "{Robot.population} "robots working")
        

    @classmethod      
    def how_many(cls):
        print("we have",{cls.population},"robots.")
    
print(Robot.population)        
siri = Robot("siri", 20161399) # 1
team = Robot("jhon" , 19171399) #2
kal = Robot("luka", 132456789) # 3
lus = Robot("lon", 132456789) # 4

Robot.die() # Robot = cls  , Robot 안에 있는 population을 측정 

################################################################

class Robot:

    """
    [Robot Class]
    Date : ??:??:??
    Author : Amaco
    """

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."

    @staticmethod
    def are_you_robot():
        print("yes!!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call!")
        return f"{self.name} call!!"


droid1 = Robot("R2-D2")
droid1.say_hi()

print(dir(droid1))

print(droid1)  # <__main__.Robot object at 0x7fde1c742110> -> R2-D2 robot!!


droid1()
########################################################################################

class Robot:

    """
    [Robot Class]
    Date : ??:??:??
    Author : Amaco
    """


    def __init__(self, name):
        self.name = name
   

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."

    @staticmethod
    def are_you_robot():
       
        print("yes!!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call!")
        return f"{self.name} call!!"
    
    
class Siri(Robot):
    def call_me(self):
        print("네?")
    
    def cal_mul(self,a,b):
        self.a = a 
        return a*b
    
    def name(self, name):
        print(self.name)
        
    @classmethod
    def hello_apple(cls):
        print(f"{cls}hello apple")

siri = Siri("luka")
siri.call_me()
print(siri.cal_mul(7,8))
print(siri.name)
print(siri.a)
siri.hello_apple()
print(siri.cal_mul(7,8))

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



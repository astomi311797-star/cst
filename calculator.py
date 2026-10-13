class Calculator:
    def add(self,a,b):
        self.new_x =a
        self.new_y =b
        result= self.new_x + self.new_y 
        return result
    
    def sub(self,a,b):
        self.new_x =a
        self.new_y =b
        result= self.new_x - self.new_y 
        return result
    
    def mul(self,a,b):
        self.new_x =a
        self.new_y =b
        result= self.new_x * self.new_y 
        return result
    
    def div(self,a,b):
        self.new_x =a
        self.new_y =b
        result= self.new_x / self.new_y 
        return result
    
    def mod(self,a,b):
        self.new_x =a
        self.new_y =b
        result= self.new_x % self.new_y 
        return result
    
    
    
calc = Calculator()
n1=(int(input("enter first number :")))
n2 = (int(input("enter second number:")))
Add = calc.add(n1 ,n2)
print(Add)
print(calc.sub(int(input("enter first number :")) ,(int(input("enter second number :")))))
print(calc.mul(int(input("enter first number :")) ,int(input("enter second number :"))))
print(calc.div(int(input("first number =")) ,int(input("first number ="))))
print(calc.mod(int(input("first number =")) ,int(input("first number ="))))


def sum(num1,num2):
	return num1+num2

def info(weight,height,name,**kwargs):
	print(weight,height,name)
	print(kwargs)

company='파이썬 주식회사'

class Calculator:
    first = 0
    second = 0
    
    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second
        
    def setData(self, first=None, second=None):
        self.first = first
        self.second = second
        
    def sum(self):
        return self.first + self.second
    
    def div(self):
        return self.first / self.second
    
    def mul(self):
        return self.first * self.second
    
    def sub(self):
        return self.first - self.second
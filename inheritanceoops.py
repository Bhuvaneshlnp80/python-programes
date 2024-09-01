#oops concept
#inheritance 

class engine():
    tankcapacity=10
    def __init__(self):
        self.petrol=True
    def enginestarts(self):
        print('smooth engine sound')
class car():
    def __init__(self):
        self.engine=engine()
    def petrol(self):
        self.engine.enginestarts()
        print(engine.tankcapacity)
    
c=car()
c.petrol()


class a2():
    def __init__(self):
        self.price=10

class a3(a2):
    def __init__(self):
        super().__init__()
        self.prices=15
a4=a3()
print(a4.price)


class employee():
    def __init__(self,name,age):
        self.name=name
        self.age=age
class employees(employee):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def __str__(self):
        return 'name={} \nsalary={}'.format(self.name,self.salary)
        
emp1=employees('bhuvi',20,150000)
print(emp1)

#overloading
class mobile():
    def __init__(self,brand,price,offer):
        self.brand=brand
        self.price=price
        self.offer=offer
    def __lt__(self,other):
        return self.price<other.price
    
    def __add__(self,other):
        return self.offer+other.ccoffer
class creditcard():
    def __init__(self,brand,ccoffer):
        self.brand=brand
        self.ccoffer=ccoffer
        
m1=mobile('vivo',10000,1000)
cc=creditcard('iq',2000)
print(m1+cc)

m2=mobile('sam',15000,1500)
print(m1<m2)
#calling private function from outside of the class
class bhuvi():
    a=1
    __b=12
    def __init__(self):
        self.__c=10
    def me(self):
        print(bhuvi.a)
        print(bhuvi.__b)
        
t=bhuvi()
t.me()
print(t._bhuvi__c)



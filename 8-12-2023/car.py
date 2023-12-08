#create a class car wiith attributes color price and kilometres and compare
#the price of two cars and add the total kilo metres of 2 cars
class Car:
    def __init__(self,color,price,km):
        self.color = color
        self.price = price
        self.km = km
    def __gt__(self,others):
        if(self.price>others.price):
            return True
        else:
            return False
    def __add__(self,others):
        return self.km+others.km
c1=Car("Black",1200,2000)
c2=Car("Red",1500,5800)
if(c1>c2):
     print("Car1 price is high")
else:
    print("Car 2 price is high")
print(c1+c2)
           
        
            



    

    

        
    

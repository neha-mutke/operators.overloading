class book:
    def __init__(self,n,p):
        self.name=n
        self.price=p

    def __add__(self,other):
        return self.price + other.price 
    
    def __sub__(self,other):
        return self.price - other.price 

    def __mul__(self,other):
        return self.price * other.price   
    
    def __truediv__(self,other):
        return self.price / other.price 
    
    def __floordiv__(self,other):
        return self.price // other.price 
    
    def __mod__(self,other):
        return self.price % other.price 
    
    def __pow__(self,other):
        return self.price ** other.price    
    
    def __It__(self,other):
        return self.price < other.price
    
    def __Ie__(self,other):
        return self.price <= other.price
    
    def __gt__(self,other):
        return self.price > other.price
    
    def __ge__(self,other):
        return self.price >= other.price
    
    def __eq__(self, other):
        return self.price == other.price
    
    def __nq__(self,other):
        return self.price != other.price
    
    def __iadd__(self, other):
         self.price += other.price
         return self
    
    def __isub__(self, other):
         self.price -= other.price
         return self
    
    def __imul__(self, other):
         self.price *= other.price
         return self
    
    def __idiv__(self, other):
         self.price /= other.price
         return self
    
    def __str__(self):
        return f"Book({self.name!r}, {self.price})" 



b1=book("core python",2)
b2=book("adv. python",4)
print( b1 + b2)   # 6
print( b1 - b2)   # -2
print( b1 * b2)   # 8
print( b1 / b2)   # 0.5
print( b1 // b2)  # 0
print( b1 % b2)   # 2
print( b1 ** b2)  # 16
print( b1 < b2)   # True
print( b1 <= b2)  # True
print( b1 > b2)   # False
print( b1 >= b2)  # False
print(b1 == b2)   # False
print( b1 != b2)  # True
b1 += b2
print(b1)         #Book('core python', 6)
b2 -= b1          
print(b2)         #Book('adv. python', -2)
b1 *= b2
print(b1)         #Book('core python', -12)
b1 /= b2
print(b1)          #6.0



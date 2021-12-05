#zadanie 1

def calculate(a,b,c):
    x=a*b*c
    y=a*(b+c)
    z=a+(b*c)
    if y<=x>=z:
        return x
    elif x<=y>=z:
        return y
    elif x<=z>=y:
        return z
		
#zadanie 2

def sentence(s):
    for characters in s:
        if characters.isdigit():
            return characters
        
    return False
	
# zadanie 3

def longstring(ls):
    splitted=''
    for words in ls:
        if words.isupper():splitted+=' %s' %words
        else: splitted+=words
    return splitted.lower()
	
# zadanie 4 (5?)

def listt(lst):
    result = [n for n in lst if n != 0]
    result.extend([0] * lst.count(0))
    return result
	
# zadanie 5 a

class Calculator:
    def adding(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
    
my_calc = Calculator()

while True:

    print("1: Adding")
    print("2: Subtract")
    print("3: Exit")
    
    ch = int(input("Select operation: "))
        
    if ch in (1, 2, 3):
     
       
        if(ch == 3):
            break
      
            
        a = int(input("Enter first number: "))
              
        b = int(input("Enter second number: "))
        
                   
        
        if(ch == 1):
            print(a, "+", b, "=", my_calc.adding(a, b))
        elif(ch == 2):
            print(a, "-", b, "=", my_calc.subtract(a, b))
    
    else:
        print("Unknown function!")	
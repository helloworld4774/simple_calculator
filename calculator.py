class Calculator:
   
    """Performs the four basic mathematical operations
      Starting from a initial value of 0 ("currentvalue")
  
    Methods:
     add(number) :- Adds number to current value
     subtract(number) :- Subtracts number from current value
     multiply(number) :- Multiplies number with current value
     divide(number) :- Divides number with current value
     root(number) :- Takes root to the power of number of the current value
     reset_memory() :- Resets current value to 0.
 
 
    """
    
    def __init__(self,initial = 0):
        self.currentvalue = initial
    
    def reset_memory(self):
        self.currentvalue = 0
        

    def add(self, number1, number2 = None):
        
        try:
            if number2 == None:
                number2 = self.currentvalue

            self.currentvalue = float(number1) + float(number2)
            return self.currentvalue
        except:
            return 'Invalid input'
        
        

    
    def subtract(self, number1, number2 = None):

        try:
            if number2 == None:
                number2 = self.currentvalue

            self.currentvalue = float(number2) - float(number1)
            return self.currentvalue
        except:
            return 'Invalid input'



    def multiply(self,  number1, number2 = None):
        try:
            if number2 == None:
                number2 = self.currentvalue

            self.currentvalue = float(number1) * float(number2)
            return self.currentvalue
        except:
            return 'Invalid input'



    def divide (self,  number1, number2 = None):
        try:
            if number2 == None:
                number2 = self.currentvalue

            self.currentvalue = float(number2) / float(number1)
            return self.currentvalue
        except ZeroDivisionError:
            return 'Can not divide by zero.'
        except: 
            return 'Invalid input'


    def root(self,number1,number2=None):
        try:
            if number2 == None:
                number2 = self.currentvalue

            self.currentvalue = float(float(number1) ** (1/float(number2)))
            return self.currentvalue
        except:
            return 'Invalid input'
    
    
   
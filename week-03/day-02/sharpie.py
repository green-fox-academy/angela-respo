# Create Sharpie class 
# We should know about each sharpie their color (which should be a string),
#  width (which will be a floating point number), ink_amount (another floating point number)
# When creating one, we need to specify the color and the width
# Every sharpie is created with a default 100 as ink_amount
# We can use() the sharpie objects 
# which decreases inkAmount

class Sharpie():
    def __init__(self,color,width=0.0,ink_amount=100.0):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount
    
    def use(self,inkAmount):
        try:
            if type(inkAmount) == float or type(inkAmount) == int:
                self.ink_amount -= inkAmount
                return self.ink_amount
        except:
            return None

sharpieModal = Sharpie('blue',2.0,100.0)
print(sharpieModal.use('ink'))



from resturant import Resturant
class IcecreamStand (Resturant) :
    def __init__(self, name,flavours):
        super().__init__(name)
        self.flavours = flavours
        
    def display_flavours (self) :
        for flavour in self.flavours :
            print (f'This is the {flavour} in this list')
            
    def get_info(self) :
        print (f'\nThis is the {self.name} resturant and it is the best')
class Resturant :
    def __init__(self,name) :
        self.name  = name
        self.cuisine = "Sea food"
        self.number_served = 0
        
    def print_cuisine(self ) :
        print(f" The resturant has this type of cuisine : {self.cuisine}")
        
    def print_name (self):
        print(f'You are welcome to {self.name} resturant')
        
    def get_info(self ):
        print(f" This is the {self.name} resturant and here {self.cuisine} is served ")
        
    def set_cuisine (self, new_cuisine) :
        self.cuisine = new_cuisine
        
        
    def set_number_served(self, new_number) :
        self.number_served = new_number
        
    def increment_number_served(self , new_number) :
        if new_number > 0 :
            self.number_served = new_number
        else :
            print ("Error could not increment ")
        
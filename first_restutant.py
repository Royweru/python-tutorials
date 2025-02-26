from resturant import Resturant

first_resturant = Resturant('Samaki samaki')
first_resturant.print_name()
first_resturant.get_info()

first_resturant.set_cuisine("Ugali")
first_resturant.get_info()

print(f'The resturant has so far served {first_resturant.number_served} people ')
first_resturant.set_number_served(43)
print(f'The resturant has so far served {first_resturant.number_served} people ')
first_resturant.increment_number_served(4)
print(f'The resturant has so far served {first_resturant.number_served} people ')

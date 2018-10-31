class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant name: \t'+ self.restaurant_name + '\ncuisine type: \t\t' + self.cuisine_type); return ''
    def open_restaurant(self):
       return 'the '+ self.restaurant_name + ' Restaurant is open'
    

print('\nCrash course Exercise 9.1')
''' # python crash course Exercise
9-1. Restaurant: Make a class called Restaurant The __init__() method for
Restaurant should store two attributes: a restaurant_name and a
cuisine_type Make a method called describe_restaurant() that prints these
two pieces of information, and a method called open_restaurant() that
prints a message indicating that the restaurant is open Make an instance
called restaurant from your class Print the two attributes individually,
and then call both methods
'''
class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant name: \t'+ self.restaurant_name + '\ncuisine type: \t\t' + self.cuisine_type); return ''
    def open_restaurant(self):
       return 'the '+ self.restaurant_name + ' Restaurant is open'

restaurant = Restaurant('chilliz', 'B.B.Q')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
#########################################3
print('\nCrash course Exercise 9.2')
'''
9-2. Three Restaurants: Start with your class from Exercise 9-1 Create
three different instances from the class, and call describe_restaurant()
for each instance
'''
salateen = Restaurant('salateen', 'karahi')
yameen = Restaurant('yameen', 'B.B.Q')
zahid = Restaurant('zahid', 'nahari')
print(salateen.describe_restaurant())
print(yameen.describe_restaurant())
print(zahid.describe_restaurant())

################################################
print('\nCrash course Exercise 9.3')
'''
9-3. Users: Make a class called User Create two attributes called
first_name and last_name, and then create several other attributes that
are typically stored in a user profile Make a method called
describe_user() that prints a summary of the user’s information Make
another method called greet_user() that prints a personalized greeting to
the user Create several instances representing different users, and call
both methods for each user
'''
class User(): 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0
        self.weight = 0

    def describe_user(self):
        a = {'First Name: ': self.first_name,'Last name: ' : self.last_name}
        if self.age: a['Age'] = self.age
        if self.weight: a['Weight'] =self.weight
        return a
    def greet_user(self):
        print('Welcome '+self.first_name.title() + ' ' + self.last_name.title())

amir = User('amir', 'saleem')
print(amir.describe_user())
amir.age = 27
print(amir.describe_user())
amir.weight = 55
print(amir.describe_user())

hamza = User('Hamza', 'amir')
print(hamza.describe_user())
hamza.age = 4
print(hamza.describe_user())
hamza.weight = 17
print(hamza.describe_user())

khalid = User('khalid', 'amir')
print(khalid.describe_user())
khalid.age = 4
print(khalid.describe_user())
khalid.weight = 17
print(khalid.describe_user())

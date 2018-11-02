print('Crash course Execise 9.4')
'''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166)
Add an attribute called number_served with a default value of 0 Create an
instance called restaurant from this class Print the number of customers
the restaurant has served, and then change this value and print it again
    Add a method called set_number_served() that lets you set the number
of customers that have been served Call this method with a new number and
print the value again
    Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served Call this method with any
number you like that could represent how many customers were served in,
say, a day of business
'''
class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Restaurant name: \t'+ self.restaurant_name + '\ncuisine type: \t\t' + self.cuisine_type)
        return 
    def open_restaurant(self):
       return 'the '+ self.restaurant_name + ' Restaurant is open'
    def  set_number_served(self, new_number):
        self.number_served = new_number
    def increment_number_served(self, number):
        self.number_served += number
restaurant = Restaurant('chilliz', 'Fast_food')
print(restaurant.number_served) #0
restaurant.set_number_served(20)
print(restaurant.number_served) #20
restaurant.increment_number_served(3)
print(restaurant.number_served) #23
#################################################
print('python crash course 9.5')
'''
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166) Write a method called increment_
login_attempts() that increments the value of login_attempts by 1 Write
another method called reset_login_attempts() that resets the value of
login_attempts to 0
    Make an instance of the User class and call increment_login_attempts()
several times Print the value of login_attempts to make sure it was
incremented properly, and then call reset_login_attempts() Print
login_attempts again to make sure it was reset to 0
'''
class User(): 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0
        self.weight = 0
        self.login_attempts = 0

    def describe_user(self):
        a = {'First Name: ': self.first_name,'Last name: ' : self.last_name}
        if self.age: a['Age'] = self.age
        if self.weight: a['Weight'] =self.weight
        return a
    def greet_user(self):
        print('Welcome '+self.first_name.title() + ' ' + self.last_name.title())
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
amir = User('amir', 'saleem')

for i in range(5): amir.increment_login_attempts()
print('amir.login_attempts: ' + str(amir.login_attempts))
amir.reset_login_attempts()
print('amir.login_attempts: ' + str(amir.login_attempts))


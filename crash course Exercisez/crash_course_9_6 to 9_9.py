# crash course 9.6 to 9.9
'''
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant
Write a class called IceCreamStand that inherits from the Restaurant
class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171)
Either version of the class will work; just pick the one you like better
Add an attribute called flavors that stores a list of ice cream flavors
Write a method that displays these flavors Create an instance of
IceCreamStand, and call this method
'''
import crash_course_9_1_to_9_3 as cc
class IceCreamStand(cc.Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['pista', 'mango', 'chocolate', 'crunch', 'vaneela', 'mix']
    def print_list(self):
        print('we are noted these flavors: ')
        [print(i) for i in self.flavors]; return ''
# for test:
my_flavors = IceCreamStand('karachi', 'icecream')
print(my_flavors.print_list())


##################################
'''
9-7. Admin: An administrator is a special kind of user Write a class
called Admin that inherits from the User class you wrote in Exercise 9-3
(page 166) or Exercise 9-5 (page 171) Add an attribute, privileges, that
stores a list of strings like "can add post", "can delete post", "can ban
user", and so on Write a method called show_privileges() that lists the
administrator’s set of privileges Create an instance of Admin, and call
your method
'''
class Admin(cc.User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print('*** ' + self.first_name + ' ' + self.last_name + '*** ')
        [print(i) for i in self.privileges]; return ''
amir = Admin('amir', 'saleem')
print(amir.show_privileges())

##################################
'''
9-8. Privileges: Write a separate Privileges class The class should have
one attribute, privileges, that stores a list of strings as described in
Exercise 9-7.
Move the show_privileges() method to this class Make a Privileges
instance as an attribute in the Admin class Create a new instance of
Admin and use your method to show its privileges
'''
class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        def show_privileges(self):
        print('*** ' + self.first_name + ' ' + self.last_name + '*** ')
        [print(i) for i in self.privileges]; return ''    
##################################
'''
9-9. Battery Upgrade: Use the final version of electric_car.py from this
section Add a method to the Battery class called upgrade_battery() This
method should check the battery size and set the capacity to 85 if it
isn’t already Make an electric car with a default battery size, call get_
range() once, and then call get_range() a second time after upgrading the
battery You should see an increase in the car’s range
'''
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        return "This car has a " + str(self.battery_size) + "-kWh battery."
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
# testing: 
a = Battery()
#print(a.describe_battery())
a.upgrade_battery()
#print(a.describe_battery())
##################################

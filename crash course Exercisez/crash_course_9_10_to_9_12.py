# crash course 9.10 to 9.12
'''   
9-10. Imported Restaurant: Using your latest Restaurant
class, store it in a module Make a separate file that
imports Restaurant Make a Restaurant instance, and call
one of Restaurant’s methods to show that the import
statement is working properly
'''
import Restaurant_class as rc
chilliz = rc.Restaurant('chilliz', 'B.B.Q')
print(chilliz.describe_restaurant())
###############################################
'''
9-11. Imported Admin: Start with your work from
Exercise 9-8 (page 178) Store the classes User,
Privileges, and Admin in one module Create a separate
file, make an Admin instance, and call show_privileges()
to show that everything is working correctly
'''
import classes as c
amir = c.Admin('Amir', 'saleem')
print(amir.show_privileges())
###############################################
'''
9-12. Multiple Modules: Store the User class in one
module, and store the Privileges and Admin classes in a
separate module In a separate file, create an Admin
instance and call show_privileges() to show that
everything is still working correctly
'''
import classes as c
amir = c.Admin('Amir', 'saleem')
print(amir.show_privileges())





# This file imports the Admin class and tests the program.
from admin import Admin

# Create an Admin instance and show privileges
admin_user = Admin('filip', 'hjerten', 19, 'bethany')
admin_user.describe_user()
admin_user.privileges.show_privileges()

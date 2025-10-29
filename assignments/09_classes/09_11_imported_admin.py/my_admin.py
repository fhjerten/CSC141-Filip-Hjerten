# This file imports the Admin class from user_module.py
from user_module import Admin

# Create an Admin instance and show privileges
admin_user = Admin('filip', 'hjerten', 19, 'bethany')
admin_user.describe_user()
admin_user.privileges.show_privileges()

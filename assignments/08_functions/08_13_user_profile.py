def build_profile(first, last, **user_info):

# I build a dictionary containing everything we know about a user
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile(
    'filip', 'hjerten',
    location='Pennsylvania',
    sport='golf',
    college='Albright College'
)

print(user_profile)

#8.12
def f(*sendwich):
    return sendwich

print(f('club'))
print(f('club', 'chicken'))
print(f('a', 'b','c'))


# 8.13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('amir', 'saleem', location='karachi', field='student')
print(user_profile)

# 8.14
def car_info(manufacturer, model_name, **other_info):
    a = dict()
    a ['manufacturer'] = manufacturer
    a ['model_name'] = model_name
    for b,c in other_info.items():
        a [b] = c
    return a
print(car_info('toyota', 'saloon'))
print(car_info('honda' ,'city', price='15 lac'))

##################################################
# 8.15
import plus as p
print(p.plus(2, 3))

# 8.16


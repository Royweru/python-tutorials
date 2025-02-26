
def print_kwargs(**kwargs):
    for key in kwargs:
        print("The key {} holds {} value".format(key, kwargs[key]))
        
        
def user_profile (first, last, **user_info) :
    user_info['first_name'] = first
    user_info['last_name'] = last
    
    return user_info

user_john  = user_profile("John","doe",location  = 'Kenya', age='23',status='single')
print(user_john)
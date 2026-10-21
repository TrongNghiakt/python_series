# # Cacl the total of values
# def total(*args):
#     print(sum(args))


# total(1, 2)
# total(1, 2, 3)
# total(1, 2, 3, 4)


# Create the user profile
def create_user(**kwargs):
    print(type(kwargs))
    print(kwargs)


create_user(name="John", age=30, city="New York")

create_user(name='Ronaldo', country='Portugal', age=38,
            club='Al Nassr', position='Forward')

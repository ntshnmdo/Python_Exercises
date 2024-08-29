# default parameters

def user_info(first_name, last_name, age):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")

user_info("\'nitish\'", "\'namdeo\'", "\'25\'")

# now we can make parameters default by giving default values in def. after that calling age parameter is not imp but if you call with different value then that of age parameter,
# it will print called value

# def user_info(first_name, last_name, age = 26):
#     print(f"your first name is {first_name}")
#     print(f"your last name is {last_name}")
#     print(f"your age is {age}")

# user_info("\'nitish\'", "\'namdeo\'", "\'25\'")

# we can also use 'None' , 'Unknown' types of default in def. but these defaults values should be at the end in the def parameters, otherwise it will give errors.
# def user_info(first_name, last_name = 'Unknown', age = None):
#     print(f"your first name is {first_name}")
#     print(f"your last name is {last_name}")
#     print(f"your age is {age}")

# user_info("\'nitish\'")
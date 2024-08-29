name = "      Nit     ish      "
dots = ".................."
print(name + dots)

# lstrip() method for removing left spaces.
print(name.lstrip() + dots)

# rstrip() method for removing right spaces.
print(name.rstrip() + dots)

# strip() method for removing both sides spaces.
print(name.strip() + dots)

# If you have spaces in between name variable then use replace method
print(name.replace(" ", "" ) + dots)
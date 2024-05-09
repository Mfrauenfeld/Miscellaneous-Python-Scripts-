x = input("Username: ")
y = input("Password: ")

x = x.replace('\'', '\"')
y = y.replace('\'', '\"')

print(f"SELECT * FROM users WHERE username = '{x}' AND password = '{y}'")
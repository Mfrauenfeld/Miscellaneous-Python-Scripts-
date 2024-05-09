x = input("Username: ")
y = input("Password: ")

# create a SQL query plugging those values directly in
print(f"SELECT * FROM users WHERE username = '{x}' AND password = '{y}'")

def check_passwd(username, password, min_length=8, check_username=True):
    if len(password) < min_length:
        return False
    elif check_username and username in password:
        return False
    else:
        return True


username_passwd = [
    {"username": "cisco", "password": "cisco"},
    {"username": "nata", "password": "natapass"},
    {"username": "user", "password": "123456789"},
]
user_dict = {"username": "cisco", "password": "cisco"}

print(check_passwd(**user_dict))
print(check_passwd(username="cisco", password="cisco"))

for info in username_passwd:
    print(check_passwd(**info))

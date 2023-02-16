

def password_check(username, password, *, min_length=8, check_username=True):
    if len(password) < min_length:
        return False
    elif check_username and username in password:
        return False
    else:
        return True


print(password_check("user1", "passwo#rd+", min_length=6))
print(password_check("user1", "passuse$r1w_ord", min_length=6, check_username=True))


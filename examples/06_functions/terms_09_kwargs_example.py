from pprint import pprint

# spec_sym=True, whitespace=False


def check_passwd(user, passwd, min_len=8, unique_numbers=3):
    numbers = set("0123456789")

    if len(passwd) < min_len:
        return False
    elif user.lower() in passwd.lower():
        return False
    elif len(set(passwd) & numbers) < unique_numbers:
        return False
    else:
        return True


def select_correct_passwd(user_list, **kwargs):
    correct_passwd = []
    wrong_passwd = []
    for user, password in user_list:
        correct_password = check_passwd(user, password, **kwargs)

        if correct_password:
            correct_passwd.append((user, password))
        else:
            wrong_passwd.append((user, password))
    return (correct_passwd, wrong_passwd)


data = [("user10", "sdld125fj"), ("user20", "sdf#245klfdj"), ("user30", "ssdkfser3df")]
correct, wrong = select_correct_passwd(data, min_len=5)
pprint(correct)
pprint(wrong)

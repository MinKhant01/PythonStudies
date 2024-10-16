user_logged_in = True

def authenticate(func):
    def wrapper(*args, **kwargs):
        if user_logged_in:
            result = func(*args, **kwargs)
            return result
        else:
            print("User not logged in yet")
    return wrapper

@authenticate
def view_dashboard():
    print("Viewing dashboard")

view_dashboard()
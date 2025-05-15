import re

def email_valid(email):
    """
    Validate email format
    """
    if not email:
        return True
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def check_user(username):
    """
    Validate username format
    """
    if not username:
        raise ValueError("Username cannot be empty")
    return True

def check_pwd(password):
    """
    Validate password format
    """
    if not password:
        raise ValueError("Password cannot be empty")
    
    if not re.search(r'[A-Z]', password):
        raise ValueError("Password must contain uppercase letters")
    
    if not re.search(r'\d', password):
        raise ValueError("Password must contain at least one digit")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValueError("Password must contain special characters")
    
    return True

def check_true(condition, message):
    """
    Check if condition is true
    """
    if not condition:
        raise ValueError(message)
    return True

def check_email(email):
    """
    Validate email format
    """
    if not email:
        return True
    
    if not email_valid(email):
        raise ValueError("Invalid email format")
    
    return True
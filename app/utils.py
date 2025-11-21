def validate_registration(username, email, password, confirm_password):
    if password != confirm_password:
        return "Passwords do not match."
    if len(password) < 6:
        return "Password must be at least 6 characters."
    # Add more validations as needed (e.g., email format)
    return None
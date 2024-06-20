# Brute Force Login Script

This Python script performs a brute force attack to test login credentials on a PHP application. It attempts to log in using a list of passwords provided in a text file (e.g., `rockyou.txt`).

## Dependencies

- Python 3.x
- `requests` library

Install the `requests` library using pip:

```bash
pip install requests
```

## Usage

1. **Clone Repository**:
   ```bash
   git clone https://github.com/olivierluethy/brute-force-login.git
   cd brute-force-login
   ```

2. **Download `rockyou.txt`**:
   - Download the `rockyou.txt` file (or use any other password list) from [here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt).

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `brute_force.py`.
   - Run the script:
     ```bash
     python brute_force.py
     ```
   
4. **Enter Information**:
   - Enter the login URL of your PHP application when prompted (e.g., `http://example.com/login.php`).
   - Enter the email to brute force.
   - Enter the path to the `rockyou.txt` file or another password list file.

5. **Analysis**:
   - The script attempts to log in with each password in the list.
   - It prints whether each attempt was successful or not.
   - If successful, it displays the password used.

## Notes

- **Session Handling**: The script automatically handles session management with the `requests` library. If your PHP application requires session persistence, it will maintain session cookies across requests.
- **Security**: Ensure you have explicit permission to perform brute force testing on the target PHP application. Unauthorized access attempts can be illegal and unethical.
- **Performance**: Using a large password list (`rockyou.txt` has millions of passwords) may take a significant amount of time depending on network latency and server response times.

## Example

Here's an example usage scenario:

```bash
Enter the login URL of the PHP application: http://example.com/login.php
Enter the email to brute force: admin@example.com
Enter the path to the password file: /path/to/rockyou.txt
```

This will initiate the brute force attack against the specified PHP application's login page.

### Customize:
- Replace `/path/to/rockyou.txt` with the actual path where you have downloaded the `rockyou.txt` file or any other password list file.
- Modify the GitHub repository link (`git clone ...`) to your actual repository if you're hosting it on GitHub.

## Contributions
Contributions are welcome! If you have many adjustments, create a post request.

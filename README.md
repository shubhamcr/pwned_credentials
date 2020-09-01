# Pwned Credentials
[![Flask version](https://img.shields.io/badge/flask-v1.1.2-blue)](https://flask.palletsprojects.com/en/1.1.x/)
[![Python version](https://img.shields.io/badge/python-v3.8.1-brightgreen)](https://www.python.org/)
![Open source project license](https://img.shields.io/badge/license-MIT-green)

[Pwned Credentials](https://pwnedcredentials.herokuapp.com/) is a webapp which allows users to 
securely search over multiple data breaches to determine if their password has ever been 
compromised, alongside necessary password strength recommendations. It also provides an exhaustive 
list of breached websites which includes date of breach, number of breached accounts and breached data.
Visit the website at https://pwnedcredentials.herokuapp.com/

It is built over the APIs provided by [haveibeenpwned.com](https://haveibeenpwned.com/). 
Please refer [here](https://haveibeenpwned.com/API/v3) for Have I Been Pwned Api documentation.

The pwned password service provided by Have I Been Pwned utilizes 
[k-anonymity](https://en.wikipedia.org/wiki/K-anonymity) which allows external parties to use
it and maintain anonymity. The pwned password service only requires first 5 characters of SHA-I 
password hash and returns a list of SHA-I hashes matching the first 5 characters, thus delegating the 
responsibility to the client to match the password hash against the list provided by the service. This 
ensures that the service is not aware about the full password hash and thus cannot use it to generate the 
raw password.
Please refer [here](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/) for further
details with illustrated example.


## Project setup instructions
1. Clone this repository on your local machine.
2. Make sure python 3.8 or above and pip is installed. Refer [here](https://www.python.org/downloads/)
for python installation.
3. Create and activate a virtual environment.
4. Navigate to project directory and run ```pip install -r requirements.txt``` on terminal to install 
all the project requirements.
5. Run ```export FLASK_APP=pwned_credentials.py``` on terminal to set the FLASK_APP environment
variable. Use ```set``` instead of ```export``` on Windows.
6. Execute ```flask run``` command on terminal to launch the application.
7. Navigate to http://127.0.0.1:5000/ to visit the website home page.
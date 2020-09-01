# Pwned Credentials
[Pwned Credentials](https://pwnedcredentials.herokuapp.com/) is a webapp which allows users to 
securely search over multiple data breaches to determine if their password has ever been 
compromised, alongside necessary password strength recommendations. It also provides an exhaustive 
list of breached websites which includes date of breach, number of breached accounts and breached data.

It is built over the APIs provided by [haveibeenpwned.com](https://haveibeenpwned.com/). 
Please refer [here](https://haveibeenpwned.com/API/v3) for Have I Been Pwned Api documentation.

The pwned password service provided by Have I Been Pwned utilizes 
[k-anonymity](https://en.wikipedia.org/wiki/K-anonymity) which allows external parties to use
it and maintain anonymity. The pwned password service only requires first 5 characters of SHA-I hash 
and returns a list of SHA-I hashes matching the first 5 characters, thus delegating the responsibility
to the client to match the password hash against the list provided by the service. This ensures that 
the service isnot aware about the full password hash and thus cannot use it to generate the raw password.
Please refer [here](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/) for further
details with illustrated example.


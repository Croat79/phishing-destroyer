import os
import requests
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def sendRequest(email, password, proxy):
    try:
        r = requests.post("https://servicsverfssl.serveirc.com/login/process_login.php", {
            'login_email': email,
            'login_password': password,
            'splitLoginContext': 'inputPassword',
            'isCookiedHybridEmail': 'true',
            'partyIdHash': '619ff1e381b2c4c45e138e6c4bb51aae9a4da377f2682d58eafa68d1664c26e7',
            'btnLogin': 'Login'
        }, proxies=proxy, timeout=5)
        if '<h1>404 Not Found</h1>The page that you have requested could not be found.' in r.text:
            return 1
        else:
            return 2
    except:
        return 0


def getEmail(names, lastnames):
    return f'{names[random.randint(0, len(names))]}.{lastnames[random.randint(0, len(lastnames))]}@icloud.com'.replace('\n', '').replace('\r', '')


def getPass(names):
    return f'{names[random.randint(0, len(names))].capitalize()}{random.randint(0, 2000)}'.replace('\n', '').replace('\r', '')


if __name__ == "__main__":
    f1 = open('names.txt')
    f2 = open('lastnames.txt')
    f3 = open('proxies.txt')
    names = []
    lastnames = []
    proxies = []
    for x in f1:
        names.append(x.lower())
    for x in f2:
        lastnames.append(x.lower())
    for x in f3:
        proxies.append(x.lower())
    while True:
        proxy = {'http': 'http://'+proxies[random.randint(0, len(proxies))].replace('\n', '').replace('\r', '')}
        email = getEmail(names, lastnames)
        password = getPass(names)
        result = sendRequest(email, password, proxy)
        if result == 2:
            print(f'{bcolors.OKGREEN} Sucessfully with {email}:{password}')
        elif result == 1:
            print(f'{bcolors.WARNING} IP banned with {email}:{password}')
        elif result == 0:
            print(f'{bcolors.FAIL} Connection problem or proxy dead {email}:{password}')

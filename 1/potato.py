import requests
import random
from colorama import Fore
import threading
import time
names = []
lastnames = []
success = 0
ipfail = 0
networkerror = 0


def sendRequest(email, password):
    try:
        data = {'login_email': email,
                'login_password': password,
                'splitLoginContext': 'inputPassword',
                'isCookiedHybridEmail': 'true',
                'partyIdHash': '619ff1e381b2c4c45e138e6c4bb51aae9a4da377f2682d58eafa68d1664c26e7',
                'btnLogin': 'Login'}

        url = 'https://en1eip5ym8j2ri0.m.pipedream.net'
        r = requests.post(url, data=data, timeout=2.5)
        if '<h1>404 Not Found</h1>The page that you have requested could not be found.' in r.text:
            return False
        else:
            return True
    except:
        return False


def getHost():
    return random.choice([
        'gmail.com',
        'orange.fr',
        'icloud.com',
        'yahoo.fr',
        'yahoo.com'
    ])


def getEmail(names, lastnames):
    return f'{names[random.randint(0, len(names)-1)]}.{lastnames[random.randint(0, len(lastnames)-1)]}@{getHost()}'.replace('\n', '').replace('\r', '')


def getPass(names):
    return f'{names[random.randint(0, len(names)-1)].capitalize()}{random.randint(0, 2000)}'.replace('\n', '').replace('\r', '')


def doRequest():
    while True:
        email = getEmail(names, lastnames).replace(' ','')
        password = getPass(names).replace(' ','')
        if sendRequest(email, password):
            print(f'{Fore.GREEN} Success {Fore.WHITE}{email}:{password}')
        else:
            print(f'{Fore.RED} Failed {Fore.WHITE}{email}:{password}')

if __name__ == "__main__":
    print(f'''
        {Fore.BLUE} Phishing destroyer
        {Fore.MAGENTA} Coded by Drayneur\n
    ''')
    f1 = open('names.txt')
    f2 = open('lastnames.txt')
    for x in f1:
        names.append(x.lower())
    for x in f2:
        lastnames.append(x.lower())
    threads =[]
    for i in range(50):
        t = threading.Thread(target=doRequest)
        t.deamon = True
        threads.append(t)
    for i in range(50):
        threads[i].start()
    for i in range(50):
        threads[i].join()

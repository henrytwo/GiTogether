# gitd8.py

import sys
import os
import socket
import pickle
from Thread import *
from collections import deque

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Gets the parameters from system
client.connect()
arguements = sys.argv[1:]

username = None

logo = '''                                                   
 .----.-...........-..--..---.--.......-..--.---.`
:hhhyyssoo         osyyysyyysooo        oosyyyhhdm
:hhhyo                syyyso               oshhhdm
:dhs                    oo                    yddm
:ho                                            smm
:o               ohmyo                          sm
-                 shddyo                         h
/                   shddddhs                     y
/                     mdddddo                    s
/                     ydddddyo                   y
-                      omdhhddyo                 d
:s                     omdy shddyhys            ym
:hs                    omdy   hddddds          hmm
:dhhs                  omdy   sddddds        sdmmm
:dhhyhs                omdy    osyso       sdmdhdm
:dhhyyyys              smdy              ydmdhhhdm
:dhhyyysyhyo          hmdddho         oymmhyyyhhdm
:dhhyyyssyyyyo        ddddddo       ohmmhyyyyyhhdm
:dhhyyyssyysyhyo      osyyyo      ohmdhyyyyyyyhhdm
:dhhyyyssyysyysyys              sdmdyyyyyyyyyyhhdm
:dhhyyyssyysyyssyyys          ydmdmhyyyyyyyyyyhhdm
:dhhyyyssyysyyssyysyhyo    oymmhyhmhyyyyyyyyyyhhdm
:dhhyyyyyyyyyyyyyyyyyyhyooymmdyyyhmhyyyyyyyyyhhhdm
                                                 
             ~WELCOME TO GITOGETHER~
           Dating for CS nurds in 2k17
'''

# Auto logs in if available
if os.path.exists('gitogether.token'):
    with open('gitogether.token', 'r') as token:
        username = token.read().strip()

# Saves GitHub username
def login():

    print(logo)

    global username

    # Confirms that user wants to purge old data
    if os.path.exists('gitogether.token') and not input('Rebase to login to new account? [y/N]: ') == 'y':
        return 

    print('Enter GitHub username <Case Sensitive>: ')
    username = input()

    # Saves username to file
    with open('gitogether.token', 'w') as token:
        token.write(username
                
    client.send(pickle.dumps([0, username])))
    if pickle.loads(client.recv(4096)) == 'success':
        print("Operation successful!")

def init():
    client.send(pickle.dumps([1]))

    if pickle.loads(client.recv(4096)) == 'success':
        print("Operation successful!")

people = []
people_checked = set()
current_check = ""
final = ""

message = deque()

def reciever():
    global message
    while True:
        msg = pickle.loads(client.recv(4096))

        if msg[0] == 10:
            print("Match match made with", msg[1])
            t = input("Accept?[y/n]").lower()
            client.send(pickle.dumps([9, t]))
        else:
            deque.append(msg)

p = Thread(target=reciever)
p.start()

def pull():
    global people, people_checked, current_check

    if len(people) == 0 :
        client.send(pickle.dumps([2]))
        people = message.popleft()
        people = [x for x in people if x not in people_checked]
    
    current_check = people.pop(0)
    people_checked.add(current_check)

    print(current_check)

def reject():
    global current_check

    if current_check != "":
        current_check = ""

def commit():
    global final, current_check
    
    if current_check != "":
        client.send(pickle.dumps([3, current_check]))
        final = current_check
        current_check = ""


def push():
    if final != "":
        client.send(pickle.dumps([4, final]))
        print("Waiting for approval")
        if message.popleft() == 'good':
            print("Match made. Visit V2 of the proram for more info.")
            print("Your partner's Github name is", final)

def rebase():
    global people, people_checked, current_check, final
    people = people_checked = current_check, final

    os.remove('gitogether.token')


def help():
    print('Why hello there fellow gitter, you seem to be having some issues:')
    print('help  - This page')
    print('login - Login with GitHub username')
    print('pull  - View and make pull requests [ Matches ;) ]')
    print('push  - Confirm and send request to user')

commands = {'login':login, 'init':init, 'pull':pull, 'push':push, 'rebase':rebase, 'help':help}

if arguements[0] in commands:

    try:
        commands[arguements[0]]()
    except:
        print('[Error] Dank you broke it')

else:
    print('[Error] Command "%s" not found\nEnter "help" for a list of commands' % ' '.join(arguements))


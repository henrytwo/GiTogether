# gitd8.py

import sys
import os

# Gets the parameters from system
arguements = sys.argv[1:]

username = None

logo = '''                                                   
 .----.-...........-..--..---.--.......-..--.---.`
:hhhyyssoo+++++++++osyyysyyysooo++++++++oosyyyhhdm
:hhhyo++++++++++++++++syyyso+++++++++++++++oshhhdm
:dhs++++++++++++++++++++oo++++++++++++++++++++yddm
:ho++++++++++++++++++++++++++++++++++++++++++++smm
:o+++++++++++++++ohmyo++++++++++++++++++++++++++sm
-+++++++++++++++++shddyo+++++++++++++++++++++++++h
/+++++++++++++++++++shddddhs+++++++++++++++++++++y
/+++++++++++++++++++++mdddddo++++++++++++++++++++s
/+++++++++++++++++++++ydddddyo+++++++++++++++++++y
-++++++++++++++++++++++omdhhddyo+++++++++++++++++d
:s+++++++++++++++++++++omdy+shddyhys++++++++++++ym
:hs++++++++++++++++++++omdy+++hddddds++++++++++hmm
:dhhs++++++++++++++++++omdy+++sddddds++++++++sdmmm
:dhhyhs++++++++++++++++omdy++++osyso+++++++sdmdhdm
:dhhyyyys++++++++++++++smdy++++++++++++++ydmdhhhdm
:dhhyyysyhyo++++++++++hmdddho+++++++++oymmhyyyhhdm
:dhhyyyssyyyyo++++++++ddddddo+++++++ohmmhyyyyyhhdm
:dhhyyyssyysyhyo++++++osyyyo++++++ohmdhyyyyyyyhhdm
:dhhyyyssyysyysyys++++++++++++++sdmdyyyyyyyyyyhhdm
:dhhyyyssyysyyssyyys++++++++++ydmdmhyyyyyyyyyyhhdm
:dhhyyyssyysyyssyysyhyo++++oymmhyhmhyyyyyyyyyyhhdm
:dhhyyyyyyyyyyyyyyyyyyhyooymmdyyyhmhyyyyyyyyyhhhdm
.+++++++++++++++++++++++++++++++++++++++++++++++++
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
        return 0

    print('Enter GitHub username <Case Sensitive>: ')
    username = input()

    # Saves username to file
    with open('gitogether.token', 'w') as token:
        token.write(username)

def init():
    pass

def pull():
    pass

def push():
    pass

def rebase():
    pass

def help():
    print('Why hello there fellow gitter, you seem to be having some issues ic')
    print('help - This page')
    print('login - Login with GitHub username')
    print('pull - View and make pull requests (Matches ;))')
    print('push - ')

commands = {'login':login, 'init':init, 'pull':pull, 'push':push, 'rebase':rebase, 'help':help}

if arguements[0] in commands:

    try:
        commands[arguements[0]]()
    except:
        print('[Error] Dank you broke it')

else:
    print('[Error] Command "%s" not found\nEnter "help" for a list of commands' % ' '.join(arguements))


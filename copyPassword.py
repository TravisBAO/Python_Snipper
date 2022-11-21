#! python3

import pyperclip
import sys

PASSWORDS = {'pwd': 'Travis@0030428',
             'qc': '123457',
             'a': '12345',
             'kronos': 'Travis@0030424'}
             
print("type of sys.argv is " + str(type(sys.argv)))
print("value of sys.argv is " + str(sys.argv))
print("length of sys.argv is " + str(len(sys.argv)))


print("length of sys.argv is ")

i = 0
for anyone in sys.argv:
    print("No." + str(i) + " element is " + str(anyone))
    i = i + 1
if len(sys.argv) < 2:
    print('no password is copied')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ', account, 'copied to clipboard.')
else:
    print('There is no account named', account)


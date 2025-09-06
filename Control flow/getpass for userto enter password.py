import getpass
password = getpass.getpass(prompt='enter the password:')
if password == 'oxford':
    print('welcome to the world of python programming.')
else:
    print('incorrect password...sorry, you cannot read our book.')
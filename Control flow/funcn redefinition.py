import datetime
def showMessage(msg):
    print(msg)
showMessage('hello')
def showMessage(msg):
    now=datetime.datetime.now()
    print(msg)
    print(str(now))
showMessage('cuurrent date and time is:')
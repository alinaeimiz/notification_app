#cs50 = notifer
from notifypy import Notify


def main():
    notification = Notify()
    notification.title = title()
    notification.message = massage()
    notification.icon = icon()
    notification.send()
    
def title():
    while True:
        try:
            t = input("title: ")
            return t
        except:
            pass
        
def icon():
    while True:
        try:
            t = input('want you an icon for your notification? ')
            if t.lower() == 'yes':
                z = input('your icon address:')
                return z
            elif t.lower() == 'no':
                return './images.png'
            else:
                pass
        except:
            pass

def massage():
    while True:
        try:
            t = input("massage: ")
            return t
        except:
            pass
        
            
if __name__ == "__main__":
    main()
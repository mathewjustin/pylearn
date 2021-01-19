from pynput.keyboard import Key, Listener
from basics.dsalgos.basics.trigger_capturer import triggerClass

class mClass:
    triggerCapturer= triggerClass('','')
    def on_press(self,key):
        print('{0} pressed'.format(
            key))
        self.triggerCapturer.pushShortCuts(key)
    def on_release(self,key):
        print('{0} release'.format(
            key))
        if key == Key.esc:
            # Stop listener
            return False

cobj= mClass()
# Collect events until released
with Listener(
        on_press=cobj.on_press,
        on_release=cobj.on_release) as listener:
    listener.join()
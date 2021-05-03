from pynput.keyboard import Key
from tkinter import Tk

class triggerClass:
    init_short_cut=""
    trigger_short_cut=""
    def __init__(self,i,t):
        self.init_short_cut=i
        self.trigger_short_cut=t

    def pushShortCuts(self,key):
        if not self.init_short_cut and key==Key.ctrl_l:
            print("captured ctrl")
            self.init_short_cut=key
        if not self.trigger_short_cut and key==Key.f1:
            self.trigger_short_cut=key
        if(self.init_short_cut and self.trigger_short_cut):
            self.startPlaying()
    def removeShortCuts(self,key):
        if key==Key.ctrl_l:
            print("Removed shorts")
            self.init_short_cut=None;
            self.trigger_short_cut=None;
    def startPlaying(self):
        print(Tk().clipboard_get())
class triggerClass:
    init_short_cut=""
    trigger_short_cut=""
    def __init__(self,i,t):
        self.init_short_cut=i
        self.trigger_short_cut=t

    def pushShortCuts(self,key):
        if not self.init_short_cut:
            self.init_short_cut=key
        if not self.trigger_short_cut:
            self.trigger_short_cut=key


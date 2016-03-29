
import datetime
import time
import SendKeys

try:
    import wx
except ImportError:
    print 'You don\'t have wxPython. http://www.wxpython.org/download.php'

try:
    import pyHook
except ImportError:
    print 'You don\'t have pyHook.\
    http://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/'

class LeagueFrame(wx.Frame):
    """Creates the GUI interface for the League of Legends keyboard hook"""
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,300))


        # On exit
        self.Bind(wx.EVT_CLOSE, self.onClose)
        
        
        # Timer
        self.blueTimer = wx.Timer(self, wx.ID_ANY)
        self.blueCount = 0
        self.Bind(wx.EVT_TIMER, self.blueGolem, self.blueTimer)
        
        self.redTimer = wx.Timer(self, wx.ID_ANY)
        self.redCount = 0
        self.Bind(wx.EVT_TIMER, self.redLizard, self.redTimer)
        
        self.dragonTimer = wx.Timer(self, wx.ID_ANY)
        self.dragonCount = 0
        self.Bind(wx.EVT_TIMER, self.dragon, self.dragonTimer)
        
        self.baronTimer = wx.Timer(self, wx.ID_ANY)
        self.baronCount = 0
        self.Bind(wx.EVT_TIMER, self.baron, self.baronTimer)
        
##        # For missing calls
##        self.toggle = 0
        
        # Application Menu
        
        # File
        self.fileMenu = wx.Menu()
        self.menuAboot = self.fileMenu.Append(wx.ID_ABOUT,'&About',
                            ' Information about this program')
        self.Bind(wx.EVT_MENU, self.aboot, self.menuAboot)
        self.fileMenu.AppendSeparator()
        self.menuClose = self.fileMenu.Append(wx.ID_EXIT, 'E&xit', 
                                                ' Terminate the program.')
        self.Bind(wx.EVT_MENU, self.mExit, self.menuClose)        
            
##        # Lane
##        self.laneMenu = wx.Menu()
##        self.laneTop = self.laneMenu.AppendRadioItem(-1, 'Top Lane',
##                                    'Checking this will make F1 '+
##                                    'announce missing heros from the top lane')
##        self.laneMid = self.laneMenu.AppendRadioItem(-1, 'Middle Lane',
##                                    'Checking this will make F1 announce'+
##                                    ' missing heros from the middle lane')
##        self.laneBot = self.laneMenu.AppendRadioItem(-1, 'Bottom Lane',
##                                    'Checking this will make F1 announce'+
##                                    ' missing heros from the bottom lane')

        # Menu Bar
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.fileMenu, '&File')
##        self.menuBar.Append(self.laneMenu, 'Lane')        
        self.SetMenuBar(self.menuBar)
        self.CreateStatusBar()
        
        # Panel
        self.panel = wx.Panel(self, wx.ID_ANY, pos=(0,0))

        # Buttons
        self.blueBtn = wx.Button(self.panel, wx.ID_ANY, 'Blue Golem')
        self.Bind(wx.EVT_BUTTON, self.blueGolemStart, self.blueBtn)
        self.blueText = wx.StaticText(self.panel, wx.ID_ANY, 'Golem up')
        
        self.redBtn = wx.Button(self.panel, wx.ID_ANY, 'Red Lizard')
        self.Bind(wx.EVT_BUTTON, self.redLizardStart, self.redBtn)
        self.redText = wx.StaticText(self.panel, wx.ID_ANY, 'Lizard up')
        
        self.dragonBtn = wx.Button(self.panel, wx.ID_ANY, 'Dragon')
        self.Bind(wx.EVT_BUTTON, self.dragonStart, self.dragonBtn)
        self.dragonText = wx.StaticText(self.panel, wx.ID_ANY, 'Dragon up')
        
        self.baronBtn = wx.Button(self.panel, wx.ID_ANY, 'Baron')
        self.Bind(wx.EVT_BUTTON, self.baronStart, self.baronBtn)
        self.baronText = wx.StaticText(self.panel, wx.ID_ANY, 'Baron up')

        self.blueGauge = wx.Gauge(self.panel, wx.ID_ANY, 300, size=(250,23))
        
        self.redGauge = wx.Gauge(self.panel, wx.ID_ANY, 300, size=(250,23))
        
        self.dragonGauge = wx.Gauge(self.panel, wx.ID_ANY, 360, size=(250,23))
        
        self.baronGauge = wx.Gauge(self.panel, wx.ID_ANY, 480, size=(250,23))

        # Sizers
        self.sizer = wx.FlexGridSizer(rows=0, cols=3, vgap=6, hgap=6)
        self.sizerV = wx.BoxSizer(wx.VERTICAL)
        self.sizerH = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerV.AddSizer(self.sizerH, 0, wx.ALIGN_CENTER)
        self.sizerH.AddSizer(self.sizer, 0, wx.TOP, 40)
        
        self.sizer.AddMany([self.blueBtn, self.blueGauge, self.blueText,
                            self.redBtn, self.redGauge, self.redText, 
                            self.dragonBtn, self.dragonGauge, self.dragonText,
                            self.baronBtn, self.baronGauge, self.baronText])
        
        self.panel.SetSizer(self.sizerV)
        
        self.Show(True)

    # Methods
    
    def onClose(self, event):
        hm.__del__
        self.Destroy()
        
    def aboot(self, event):
        """Menu --> About"""
        
        self.awesome = wx.MessageDialog(self, 
                    'Questions or comments: Smith7929@gmail.com', 
                    'About', wx.OK)
                
        self.awesome.ShowModal()
        self.awesome.Destroy()
        
    def mExit(self, event):
        """Menu --> File --> Exit"""
        hm.__del__
        self.Destroy()
    
    def blueGolem(self, event):
        self.blueCount = self.blueCount + 1
        self.blueGauge.SetValue(self.blueCount)
        self.blueText.SetLabel('%d seconds' % (300 - self.blueCount))
        
        if self.blueCount == 270:
                wx.Sound.PlaySound(
                'C:\Users\Zac\Dropbox\Python\Misc Scripts\lol\Golem.wav')
                
        if self.blueCount == 300:
            self.blueTimer.Stop()
            self.blueText.SetLabel('Golem up')
        
    def blueGolemStart(self, event):
        self.blueCount = 0
        self.blueGauge.SetValue(0)
        self.blueTimer.Start(1000)
        
    def redLizard(self, event):
        self.redCount = self.redCount + 1
        self.redGauge.SetValue(self.redCount)
        self.redText.SetLabel('%d seconds' % (300 - self.redCount))
        
        if self.redCount == 270:
            wx.Sound.PlaySound(
                'C:\Users\Zac\Dropbox\Python\Misc Scripts\lol\Lizard.wav')
        
        if self.redCount == 300:
            self.redTimer.Stop()
            self.redText.SetLabel('Lizard up')

    def redLizardStart(self, event):
        self.redCount = 0
        self.redGauge.SetValue(0)
        self.redTimer.Start(1000)

    def dragon(self, event):
        self.dragonCount = self.dragonCount + 1
        self.dragonGauge.SetValue(self.dragonCount)
        self.dragonText.SetLabel('%d seconds' % (360 - self.dragonCount))
        
        if self.dragonCount == 330:
            wx.Sound.PlaySound(
                'C:\Users\Zac\Dropbox\Python\Misc Scripts\lol\Dragon.wav')
        
        if self.dragonCount == 360:
            self.dragonTimer.Stop()
            self.dragonText.SetLabel('Dragon up')
        
    def dragonStart(self,event):
        self.dragonCount = 0
        self.dragonGauge.SetValue(0)
        self.dragonTimer.Start(1000)
        
    def baron(self, event):
        self.baronCount = self.baronCount + 1
        self.baronGauge.SetValue(self.baronCount)
        self.baronText.SetLabel('%d seconds' % (480 - self.baronCount))
        
        if self.baronCount == 450:
            wx.Sound.PlaySound(
            'C:\Users\Zac\Dropbox\Python\Misc Scripts\lol\Baron.wav')
            
        if self.baronCount == 480:
            self.baronTimer.Stop()
            self.baronText.SetLabel('Baron up')
            
        
    def baronStart(self, event):
        """Starts the baron timer"""
        self.baronCount = 0
        self.baronGauge.SetValue(0)
        self.baronTimer.Start(1000)
                    
    def blueReport(self, event):
        hm.UnhookKeyboard()
        if wx.GetKeyState(wx.WXK_CAPITAL):
            SendKeys.SendKeys(
                        '{CAPSLOCK}', pause=0.02, turn_off_numlock=False)
        SendKeys.SendKeys(
            '{ENTER}Blue{SPACE}spawn:{SPACE}%d{SPACE}seconds.{ENTER}' 
            % (300 - self.blueCount), pause=0.02, turn_off_numlock=False)
        hm.HookKeyboard()
        
    def redReport(self,event):
        hm.UnhookKeyboard()
        if wx.GetKeyState(wx.WXK_CAPITAL):
            SendKeys.SendKeys(
                        '{CAPSLOCK}', pause=0.02, turn_off_numlock=False)
        SendKeys.SendKeys(
            '{ENTER}Lizard{SPACE}spawn:{SPACE}%d{SPACE}seconds.{ENTER}' 
            % (300 - self.redCount), pause=0.02, turn_off_numlock=False)
        hm.HookKeyboard()
        
    def dragonReport(self,event):
        hm.UnhookKeyboard()
        if wx.GetKeyState(wx.WXK_CAPITAL):
            SendKeys.SendKeys(
                        '{CAPSLOCK}', pause=0.02, turn_off_numlock=False)
        SendKeys.SendKeys(
            '{ENTER}Dragon{SPACE}spawn:{SPACE}%d{SPACE}seconds.{ENTER}' 
            % (360 - self.dragonCount), pause=0.02, turn_off_numlock=False)
        hm.HookKeyboard()
                                 
    def baronReport(self, event):
        hm.UnhookKeyboard()
        if wx.GetKeyState(wx.WXK_CAPITAL):
            SendKeys.SendKeys(
                        '{CAPSLOCK}', pause=0.02, turn_off_numlock=False)
        SendKeys.SendKeys(
            '{ENTER}Baron{SPACE}spawn:{SPACE}%d{SPACE}seconds.{ENTER}' 
            % (480 - self.baronCount), pause=0.02, turn_off_numlock=False)
        hm.HookKeyboard()

def OnKeyboardEvent(event): 
        
    print event.KeyID
    if event.KeyID == 112:
        myFrame.blueGolemStart(event)
        
    if event.KeyID == 113:
        myFrame.redLizardStart(event)
    
    if event.KeyID == 114:
        myFrame.dragonStart(event)
        
    if event.KeyID == 116:
        myFrame.blueReport(event)
    
    if event.KeyID == 117:
        myFrame.redReport(event)
        
    if event.KeyID == 118:
        myFrame.dragonReport(event)
    
    if event.KeyID == 120:
        myFrame.baronStart(event)
        
    if event.KeyID == 121:
        myFrame.baronReport(event)
        
    
        
    
# return True to pass the event to other handlers
    return (event.KeyID not in [112,113,114,116,117,118,120,121])

# Setting the keyboard hook
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

# Instantiating the app
myApp = wx.App(False)
myFrame = LeagueFrame(None, 'League of Legends Hook')

# Launching the app
myApp.MainLoop()
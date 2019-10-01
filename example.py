# dracaryS
# for metin2devs
# 2.10.2019 00:54


#open root/game.py


#######################################

# Search

class GameWindow(ui.ScriptWindow):

# add before

Timer = ui.QueuePython()
TimerCount = 0

#######################################

# Search

def StartGame(self):

# add before 

	def TestTimer(self):
		if TimerCount != 5: 
			chat.AppendChat(chat.CHAT_TYPE_INFO, "HALO")
			TimerCount+=1
			return 2 # next event time
		return 0 # clear event <>

#######################################

# Search

def StartGame(self):

# add after

Timer.AppendEvent("test",self.TestTimer,2)

##########################################

# Search

self.interface.BUILD_OnUpdate()

# add after

Timer.Process()

##########################################


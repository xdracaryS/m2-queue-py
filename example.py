# dracaryS
# for metin2devs
# 2.10.2019 00:54

#update
# 2.10.2019 12:48

# Special thanks for vegaS

#open root/game.py

#######################################

# Search

def StartGame(self):

# add before 

	def TestTimer(self):
		global TimerCount
		if TimerCount != 5: 
			chat.AppendChat(chat.CHAT_TYPE_INFO, "hi this is turkish kebab")
			TimerCount+=1
			return 2 # next event time
		return 0 # clear event <>

#######################################

# Search

def StartGame(self):

# add after

event_create.AppendEvent("test",self.TestTimer,2)

##########################################

# Search

self.interface.BUILD_OnUpdate()

# add after

event_create.Process()

##########################################


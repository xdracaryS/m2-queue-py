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

	def TestTimer(self,level,name):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "hi this is turkish kebab level=%d name=%s"%(level,name))
		return 2 # next event time

#######################################

# Search

def StartGame(self):

# add after

event_create.AppendEvent("test",2,self.TestTimer,(player.GetLevel(),player.GetName()))

##########################################

# Search

self.interface.BUILD_OnUpdate()

# add after

event_create.Process()

##########################################


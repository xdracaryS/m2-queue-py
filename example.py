# dracaryS
# for metin2devs
# 2.10.2019 00:54

#update
# 2.10.2019 12:48

#update 10.10.2019 13:55

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

# vegaS example 

# ex1
event_create.AppendEvent(eventName='RUN', eventStartTime=0, eventFunc=self.Run)
# ex2
event_create.AppendEvent(eventName='RUN', eventStartTime=0, eventFunc=self.Run, eventFuncArgs=player.GetLevel())
# ex3
event_create.AppendEvent(eventName='RUN', eventStartTime=0, eventFunc=self.Run, eventFuncArgs=(player.GetLevel(), player.GetName()))
# ex4
event_create.AppendEvent('UPDATE', 0, self.Update, {'data' : (1, True, (14, 12), [5, 1], 'Corsair')})
# Others:
if event_create.GetEvent('RUN'):
    print ("The event exists.")
if event_create.GetIsLockedEvent('RUN'):
    print ("The event exists but is locked.")
    
event_create.LockEvent('RUN')
event_create.UnlockEvent('RUN')
event_create.DeleteEvent('RUN')


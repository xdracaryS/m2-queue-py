# dracaryS
# for metin2devs
# 2.10.2019 00:54

#update
# 2.10.2019 12:48

# update 10.10.2019

# update 11.10.2019 04:44

# Special thanks for vegaS & ulubey4242

class Queue(object):
    EXIT = 0
    def __init__(self):
        self.eventList = []
        self.eventLockedList = []
    def __del__(self):
        del self.eventList
        del self.eventLockedList
    def GetEvent(self, eventName):
        """ Get the event dictionary by specific name. """
        for event in self.eventList:
            if event['name'] == eventName:
                return event
        return None
        
    def GetIsLockedEvent(self, eventName):
        """ Get a boolean if a specific event is locked. """
        for event in self.eventLockedList:
            if event['name'] == eventName:
                return True
        return False
        
    def LockEvent(self, eventName):
        """ Lock a specific event by name for being processed. """
        event = self.GetEvent(eventName)
        if event and not event in self.eventLockedList:
            self.eventLockedList.append(event)
            
    def UnlockEvent(self, eventName):
        """ Unlock a specific event by name for being processed. """
        event = self.GetEvent(eventName)
        if event in self.eventLockedList:
            self.eventLockedList.remove(event)
            
    def DeleteEvent(self, eventName):
        """ Delete a specific event by name instantly. """
        event = self.GetEvent(eventName)
        if event:
            self.eventList.remove(event)
            
    def ResetTimeEvent(self, eventName):
        """ Reset time of a specific event by name. """
        event = self.GetEvent(eventName)
        if event:
            index = self.eventList.index(event)
            self.eventList[index] = app.GetGlobalTimeStamp()
        
    def AppendEvent(self, eventName, eventStartTime, eventRunCount, eventFunc, eventFuncArgs = ()):
		""" Append a new event by specific arguments. """
        if not eventName or not isinstance(eventStartTime, int) or not isinstance(eventRunCount, int) or not callable(eventFunc):
            return

		if self.GetEvent(eventName):
			self.DeleteEvent(eventName)

		if not hasattr(type(eventFuncArgs), '__iter__'):
			eventFuncArgs = tuple([eventFuncArgs])

		self.eventDict.update({
				str(eventName) : {
					'func' : __mem_func__(eventFunc),
					'args' : eventFuncArgs,
					'time' : int(app.GetGlobalTimeStamp() + eventStartTime),
					'locked' : False,
					'curr_run_count' : eventRunCount,
				},
			})

	def Process(self):
		""" Processing the events. """
		for event in self.eventDict:
			if event['locked']:
				continue

			if app.GetGlobalTimeStamp() >= event['time']:
				result = apply(event['func'], event['args'])
				event['curr_run_count'] -= 1

				if result in (None, self.EXIT) or not event['curr_run_count']:
					del event
					continue

				event['time'] = app.GetGlobalTimeStamp() + result


event_create = Queue()
import __builtin__
__builtin__.event_create = event_create

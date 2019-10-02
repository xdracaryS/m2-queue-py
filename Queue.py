# dracaryS
# for metin2devs
# 2.10.2019 00:54

# Special thanks for vegaS

#import types﻿
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
	def AppendEvent(self, eventName, eventStartTime, eventFunc, eventFuncArgs = ()):
		""" Append a new event by specific arguments. """
		#if not eventName or not type(eventStartTime) == int or not isinstance(eventFunc, types.MethodType):
		#	return﻿﻿
		if self.GetEvent(eventName):
			return
		if not hasattr(type(eventFuncArgs), '__iter__'):
			eventFuncArgs = tuple([eventFuncArgs])
		self.eventList.append({'name' :str(eventName), 'function' : __mem_func__(eventFunc), 'arguments' : eventFuncArgs, 'run_next_time' : int(app.GetGlobalTimeStamp() + eventStartTime)})
	def Process(self):
		""" Processing the events. """
		for index, event in enumerate(self.eventList):
			if event in self.eventLockedList:
				continue
			if app.GetGlobalTimeStamp() > event['run_next_time']:
				result = 0
				if event['arguments']:
					result = apply(event['function'], event['arguments'])
				else:
					result = event['function']()
				if result == self.EXIT:
					del self.eventList[index]
					continue
				event['run_next_time'] = app.GetGlobalTimeStamp() + result

event_create = Queue()
import __builtin__
__builtin__.event_create = event_create

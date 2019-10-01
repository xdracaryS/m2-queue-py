# dracaryS
# for metin2devs
# 2.10.2019 00:54

class QueuePython(object):
	def __init__(self):
		self.eventList=[]
	def __del__(self):
		if len(self.eventList) > 0:
			self.eventList.clear()
	def Process(self):
		if len(self.eventList) > 0:
			for j in xrange(len(self.eventList)):
				if app.GetTime() > self.eventList[j]["time"]:
					i = self.eventList[j]["func"]()
					if i == 0:
						self.eventList[j].clear()
					else:
						self.eventList[j]["time"] = app.GetTime()+i
	def AppendEvent(self,name,func,time):
		self.eventList.append({"name":str(name),"func":__mem_func__(func),"time":int(app.GetTime()+time)})

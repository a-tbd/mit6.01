class Hammock:
	def __init__(self):
		self.state = 0
		self.lastReq = ''

	def sitDown(self, name):
		if self.state == 0:
			self.lastReq = name
			self.state += 1
			print "welcome!"
		elif self.state != 0 and (self.lastReq == name):
			self.state += 1
			print "welcome!"
		else:
			self.lastReq = name
			print "sorry, no room"

	def leave(self):
		if self.state - 1 >= 0:
			self.state -= 1
			print self.state
		else:
			print self.state

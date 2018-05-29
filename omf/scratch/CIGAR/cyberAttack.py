class AlertAgent(object):
	__slots__ = 'alertTime'
	# e.g. "2000-00-03 12:00:00"
	
	def __init__(self, alertTime):
		self.alertTime = alertTime

	def readStep(self, time):
		if time == self.alertTime:
			print '!!!!!Alerting because it is now ', self.alertTime, '!!!!!!!'
			return [{'cmd':'readClock'}]
		return []

	def writeStep(self, time, rezList):
		return []

class ReadAttackAgent(object):
	__slots__ = 'attackTime', 'obNameToAttack', 'obPropToAttack'
	# e.g. "2000-01-03 12:00:00", "tm_1", "measured_power"
	
	def __init__(self, attackTime, obNameToAttack, obPropToAttack):
		self.attackTime = attackTime
		self.obNameToAttack = obNameToAttack
		self.obPropToAttack = obPropToAttack

	def readStep(self, time):
		if time == self.attackTime:
			return [{'cmd':'read','obName':self.obNameToAttack,'propName':self.obPropToAttack}]
		return []

	def writeStep(self, time, rezList):
		return []

class ReadIntervalAttackAgent(object):
	__slots__ = 'attackStartTime', 'attackEndTime', 'obNameToAttack', 'obPropToAttack'
	# e.g. "2000-01-02 08:00:00", "2000-01-03 08:00:00", "tm_1", "measured_real_energy"
	# reads the same object and property for each step between the given interval (attackStartTime and attackEndTime)
	
	def __init__(self, attackStartTime, attackEndTime, obNameToAttack, obPropToAttack):
		self.attackStartTime = attackStartTime
		self.attackEndTime = attackEndTime
		self.obNameToAttack = obNameToAttack
		self.obPropToAttack = obPropToAttack

	def readStep(self, time):
		if time >= self.attackStartTime and time <= self.attackEndTime:
			return [{'cmd':'read','obName':self.obNameToAttack,'propName':self.obPropToAttack}]
		return []

	def writeStep(self, time, rezList):
		return []

class WriteAttackAgent(object):
	__slots__ = 'attackTime', 'obNameToAttack', 'obPropToAttack', 'propTarget'
	# e.g. e.g. "2000-01-02 16:00:00", "tm_1", "measured_real_energy", "0.0"

	def __init__(self, attackTime, obNameToAttack, obPropToAttack, propTarget):
		self.attackTime = attackTime
		self.obNameToAttack = obNameToAttack
		self.obPropToAttack = obPropToAttack
		self.propTarget = propTarget

	def readStep(self, time):
		return [] # Doesn't need to read.

	def writeStep(self, time, rezList):
		if time == self.attackTime:
			#print '!!!!! Just changed the', self.obPropToAttack, 'of', self.obNameToAttack,'to',self.propTarget,'!!!!!!!!!'
			return [{'cmd':'write','obName':self.obNameToAttack,'propName':self.obPropToAttack,'value':self.propTarget}]	
		return []

class WriteIntervalAttackAgent(object):
	__slots__ = 'attackStartTime', 'attackEndTime', 'obNameToAttack', 'obPropToAttack', 'propTarget'
	# e.g. e.g. "2000-01-02 16:00:00", "tm_1", "measured_real_energy", "0.0"

	def __init__(self, attackStartTime, attackEndTime, obNameToAttack, obPropToAttack, propTarget):
		self.attackStartTime = attackStartTime
		self.attackEndTime = attackEndTime
		self.obNameToAttack = obNameToAttack
		self.obPropToAttack = obPropToAttack
		self.propTarget = propTarget

	def readStep(self, time):
		return [] # Doesn't need to read.

	def writeStep(self, time, rezList):
		if time >= self.attackStartTime and time <= self.attackEndTime:
			#print '!!!!! Just changed the', self.obPropToAttack, 'of', self.obNameToAttack,'to',self.propTarget,'!!!!!!!!!'
			return [{'cmd':'write','obName':self.obNameToAttack,'propName':self.obPropToAttack,'value':self.propTarget}]	
		return []

# class DefendOutput(object):
# 	__slots__ = 'obNameToDefend', 'obPropToDefend', 'propTarget'
# 	# e.g. "Test_inverter_1", "V_Out", "3.0"

# 	def __init__(self, obNameToDefend, obPropToDefend, propTarget):
# 		self.obNameToDefend = obNameToDefend
# 		self.obPropToDefend = obPropToDefend
# 		self.propTarget = propTarget

# 	def readStep(self, time):
# 		return [] # Doesn't need to read.

# 	def writeStep(self, time, rezList):
# 		return [{'cmd':'write','obName':self.obNameToDefend,'propName':self.obPropToDefend,'value':self.propTarget}]
class School:
	def __init__(self, name=None, roster={}):
		self.name = name
		self.roster = roster

	def add_student(self, name, grade):
		if grade not in self.roster.keys():
			self.roster[grade] = [name]
		else:
			self.roster[grade].append(name)

	def grade(self, grade):
		return self.roster[grade]

	def sort_roster(self):
		for key in self.roster:
			self.roster[key].sort()
		return self.roster
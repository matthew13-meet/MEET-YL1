class integer(object):
	def __init__(self, num, negative):
		self.num = num
		self.negative=negative

	def display(self):
		print self.num
		print self.negative

if __name__=="__main__":
	test = integer(3, "negative")
	test.display()

class NegativeInteger(integer):
	def __init__(self, number):
		super(NegativeInteger, self).__init__(number,"negative")



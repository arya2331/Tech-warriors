class Person(object):

	def __init__(self,name,age=20):
		self.name=name
		self.age=age

	def get_name(self):
	    return self.name

    def set_name(self,new_name):
    	self.name=new_name



p1=Person('Ram',25)
p2=Person('Bob')

p1.name
p1.get_name()

	p1.name='DSDS'
	p1.set_name('DSDS')
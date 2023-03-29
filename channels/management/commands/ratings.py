from django.core.management.base import BaseCommand, CommandError
from channels.models import Channel

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    data = {}
    def rating_calc_rec(self, c):

    	if c.content:
    		self.data[c.id] =  float(c.content.rating)
    		return c.content.rating
    	else:
    		rating = 0
    		for i in c.children.all():
    			rating += self.rating_calc_rec(i)
    		if rating == 0:
    			self.data[c.id] =  rating
    			return 0
    		self.data[c.id] = float(rating/len(c.children.all()))
    		return rating/len(c.children.all())

    def rating_calc(self):

    	root = Channel.objects.filter(parent = None)

    	for c in root:
    		self.rating_calc_rec(c)

    def writre_csv(self):
    	with open('rating.csv','w') as file:
    		file.write(str(self.data))

    def handle(self,*args, **kargs):

    	self.rating_calc()
    	self.writre_csv()


    


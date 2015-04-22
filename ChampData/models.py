from django.db import models


# a model for each champion that includes a name and style
class Champion(models.Model):
	name    = models.CharField('name', max_length = 255)
	#style   = models.CharField('style', max_length = 255)
	hp      = models.DecimalField('health', default = 0, max_digits=6, decimal_places=3)
	hpPlus  = models.DecimalField('health per level', default = 0, max_digits=6, decimal_places=3)
	hp5     = models.DecimalField('health per 5', default = 0, max_digits=6, decimal_places=3)
	hp5Plus = models.DecimalField('health per 5 per level', default = 0, max_digits=6, decimal_places=3)
	mp      = models.DecimalField('mana', default = 0, max_digits=6, decimal_places=3)
	mpPlus  = models.DecimalField('mana per level', default = 0, max_digits=6, decimal_places=3)
	mp5     = models.DecimalField('mana per 5', default = 0, max_digits=6, decimal_places=3)
	mp5Plus = models.DecimalField('mana per 5 per level', default = 0, max_digits=6, decimal_places=3)
	ad      = models.DecimalField('attack damage', default = 0, max_digits=6, decimal_places=3)
	adPlus  = models.DecimalField('attack damage per level', default = 0, max_digits=6, decimal_places=3)
	aSpeed  = models.DecimalField('attack speed', default = 0, max_digits=6, decimal_places=3)
	asPlus  = models.DecimalField('attack speed per level', default = 0, max_digits=6, decimal_places=1) 
	ar      = models.DecimalField('armor', default = 0, max_digits=6, decimal_places=3)
	arPlus  = models.DecimalField('armor per level', default = 0, max_digits=6, decimal_places=3)
	mr      = models.DecimalField('magic resist', default = 0, max_digits=6, decimal_places=3)
	mrPlus  = models.DecimalField('magic resist per level', default = 0, max_digits=6, decimal_places=3)
	ms      = models.IntegerField('movement speed', default = 0)
	adRange = models.IntegerField('range', default = 0)



	def __str__(self):
		return "{}".format(self.name)	



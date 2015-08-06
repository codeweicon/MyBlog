from django.db import models

# Create your models here.
class Tag(models.Model):
	tag_name = models.CharField(max_length = 40)
	def __unicode__(self):
		return self.tag_name

class Article(models.Model):
	title = models.CharField(max_length=40)
	datetime = models.DateTimeField(max_length=20)
	# tags = models.CharField(max_length=40)
	tags = models.ManyToManyField(Tag,blank = True)
	content = models.TextField()

	def __unicode__(self):
		return self.title
from django.db import models
import json

# Create your models here.
class Review(models.Model):
	categories = models.CharField(max_length=250)
	city = models.CharField(max_length=250)
	country = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	date = models.DateTimeField(max_length=250)
	rating = models.IntegerField()
	tokens = models.CharField(max_length=100000)
	# tokens = JSONField()

	class Meta:
		ordering = ("name",)
		verbose_name = "review"
		verbose_name_plural = "reviews"

	def __str__(self):
		return "{}".format(self.name)

	def set_tokens(self, x):
		self.tokens = json.dumps(x)

	def get_tokens(self, x):
		return json.loads(self.tokens)
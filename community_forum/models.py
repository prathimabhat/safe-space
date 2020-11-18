from django.db import models

# Create your models here.
class Categories(models.Model):
	class Meta:
		verbose_name_plural="Categories"

	id=models.AutoField(primary_key=True,unique=True)
	category_name=models.CharField(max_length=200,blank=True)

	def __str__(self):
		return f"{self.category_name}"
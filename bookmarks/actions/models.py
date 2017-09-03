from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Action(models.Model):
	user = models.ForeignKey(User, related_name='actions', db_index=True)

	verb = models.CharField(max_field=255)
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	class Meta:
		ordering = ('-created',)
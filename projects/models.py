from django.db import models
import uuid 

class Project(models.Model):
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
	title = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	featured_image = models.ImageField(upload_to='images/', default='default.jpg', null=True, blank=True)
	demo_link = models.CharField(max_length=500, null=True, blank=True)
	source_link = models.CharField(max_length=500, null=True, blank=True)
	tags = models.ManyToManyField('Tag', blank=True)
	vote_total = models.IntegerField(default=0, null=True, blank=True)
	vote_ratio = models.IntegerField(default=0, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Project'
		verbose_name_plural = 'Projects'

	def __str__(self):
		return self.title


class Review(models.Model):
	VOTE_TYPE = (
		('up', 'Up Vote'),
		('down', 'Down Vote'),
	)

	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
	# owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews', related_query_name='review')
	body = models.TextField(null=True, blank=True)
	value = models.CharField(max_length=200, choices=VOTE_TYPE)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Review'
		verbose_name_plural = 'Reviews'
		# unique_together = [['owner', 'project']]

	def __str__(self):
		return self.value


class Tag(models.Model):
	name = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'

	def __str__(self):
		return self.name
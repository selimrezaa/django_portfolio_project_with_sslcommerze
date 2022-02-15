from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from second_app.models import Profile


# Create your models here.

class Feedback(models.Model):
    name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    message = models.TextField(blank=False)
    star = models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(5)])
    photo=models.ImageField(upload_to="Feedback/",blank=True,default="feedback.jpg")
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{}-{}'.format(self.name, self.star)

    def get_city(self):
        get_user = Profile.objects.get(user=self)
        return "tutul"

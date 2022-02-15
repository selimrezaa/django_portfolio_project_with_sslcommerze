from os import link
from pydoc import describe
from django.db import models
from colorfield.fields import ColorField
# Create your models here.
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Delivered','Delivered'),
    )
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    status = models.CharField(max_length=255,choices=STATUS,default='Pending')

class ContactModel(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.PositiveBigIntegerField(null=True)
    email = models.EmailField(null=True)
    message = models.CharField(max_length=999,null=True)

    def __str__(self):
        return f"{self.email}"



class Header(models.Model):
    logo = models.FileField(upload_to='homeimages',null=True,blank=True)
    group_link = models.URLField(max_length=999,null=True,blank=True)


class HomePageTitleAndExtra(models.Model):
    you_get_title = models.CharField(max_length=255,null=True,blank=True)
    we_complete_title = models.CharField(max_length=255,null=True,blank=True)
    client_review_title = models.CharField(max_length=255,null=True,blank=True)
    partners = models.IntegerField(default=0,null=True,blank=True)
    project_done = models.IntegerField(default=0,null=True,blank=True)
    happy_client = models.IntegerField(default=0,null=True,blank=True)


class HomePageTopSlider(models.Model):
    img = models.FileField(upload_to='homeimages',null=True,blank=True)
    def __str__(self):
        return f"{self.img.name.split('/')[-1]}"
    class Meta(object):
        ordering = ['img']


class HomePageYouGet(models.Model):
    text = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f"{self.text}"


class HomePageWeComplete(models.Model):
    text = models.CharField(max_length=255,null=True,blank=True)
    progress = models.IntegerField(default=0,null=True,blank=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return f"{self.text} (progress:{self.progress})"


class OurWorksSection(models.Model):
    section_name = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.section_name}"
class OurWorks(models.Model):
    section = models.ForeignKey(OurWorksSection,on_delete=models.CASCADE,null=True,blank=True)
    img = models.FileField(upload_to='ourworks',null=True,blank=True)
    link = models.URLField(max_length=999,null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    subtitle = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.section}"

class TeamMember(models.Model):
    img = models.FileField(upload_to='teammember',null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    subtitle = models.CharField(max_length=255,null=True,blank=True)
    describe = models.TextField(max_length=999,null=True,blank=True)
    facebook_link = models.URLField(max_length=999,null=True,blank=True)
    instagram_link = models.URLField(max_length=999,null=True,blank=True)
    whatsapp_link = models.URLField(max_length=999,null=True,blank=True)

    def __str__(self):
        return f"{self.title}"


class Footer(models.Model):
    footer_quotes= models.TextField(max_length=999,null=True,blank=True)

    footer_contact_title = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(max_length=255,null=True,blank=True,)

    footer_links_title = models.CharField(max_length=255,null=True,blank=True)
    footer_payment_title = models.CharField(max_length=255,null=True,blank=True)
    payment_logo = models.FileField(upload_to='homeimages',null=True,blank=True)

    footer_facebook_link = models.URLField(max_length=999,null=True,blank=True)
    footer_instagram_link = models.URLField(max_length=999,null=True,blank=True)
    footer_twitter_link = models.URLField(max_length=999,null=True,blank=True)
    footer_linkedin_link = models.URLField(max_length=999,null=True,blank=True)
    footer_youtube_link = models.URLField(max_length=999,null=True,blank=True)

    footer_copyright = models.CharField(max_length=255,null=True,blank=True)


class AboutUs(models.Model):
    title1 = models.CharField(max_length=255,null=True,blank=True)
    field1= models.TextField(max_length=999,null=True,blank=True)

    title2 = models.CharField(max_length=255,null=True,blank=True)
    field2= models.TextField(max_length=999,null=True,blank=True)

    title3 = models.CharField(max_length=255,null=True,blank=True)
    field3= models.TextField(max_length=999,null=True,blank=True)

    title4 = models.CharField(max_length=255,null=True,blank=True)
    field4= models.TextField(max_length=999,null=True,blank=True)

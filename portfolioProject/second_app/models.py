from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="", related_name='user_profile', blank=True,
                                null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True, default="", )
    last_name = models.CharField(max_length=25, blank=True, null=True, default="", )
    img = models.ImageField(upload_to='user_photos', blank=True, null=True, default="", )
    phone = models.CharField(max_length=15, blank=True, null=True, default="", )
    country = models.CharField(max_length=100, blank=True, null=True, default="", )
    city = models.CharField(max_length=199, blank=True, null=True, default="", )
    zip_code = models.IntegerField(blank=True, null=True, default="0", )

    def __str__(self):
        return str(self.user)

    def is_fully_filled(self):
        fields_name = [f.name for f in self._meta.get_fields()]
        for field_name in fields_name:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
        return True

class HomePageTopSlider(models.Model):
    img = models.ImageField(upload_to='homeimages', null=True, blank=True)

    def __str__(self):
        return f"{self.img.name.split('/')[-1]}"

    class Meta(object):
        ordering = ['img']


class HomePageYouGet(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(default="fa fa-envelope-open", max_length=100)

    def __str__(self):
        return f"{self.text}"


class HomePageWeComplete(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    progress = models.PositiveIntegerField(default=0, null=True, blank=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return f"{self.text} (progress:{self.progress})"


class Achievement(models.Model):
    partner = models.IntegerField()
    project_done = models.IntegerField()
    happy_client = models.IntegerField()

    def __str__(self):
        return f"{self.partner} partners"


class Footer(models.Model):
    footer_quotes = models.TextField(max_length=999, null=True, blank=True)

    footer_contact_title = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True, )

    footer_links_title = models.CharField(max_length=255, null=True, blank=True)
    footer_payment_title = models.CharField(max_length=255, null=True, blank=True)
    payment_logo = models.FileField(upload_to='homeimages', null=True, blank=True)

    footer_facebook_link = models.URLField(max_length=999, null=True, blank=True)
    footer_instagram_link = models.URLField(max_length=999, null=True, blank=True)
    footer_twitter_link = models.URLField(max_length=999, null=True, blank=True)
    footer_linkedin_link = models.URLField(max_length=999, null=True, blank=True)
    footer_youtube_link = models.URLField(max_length=999, null=True, blank=True)

    # footer_copyright = models.CharField(max_length=255,null=True,blank=True)


class BasicProduct(models.Model):
    amount_doller = models.CharField(max_length=100, blank=True, null=True)
    amonut_tk = models.CharField(max_length=100, blank=True, null=True)
    disk_space = models.BooleanField(default=True, help_text="50GB disk space", blank=True, null=True)
    email_account = models.BooleanField(default=True, help_text="50 Email Account", blank=True, null=True)
    bandwith = models.BooleanField(default=True, help_text="50GB disk spacet", blank=True, null=True)
    maintenance = models.BooleanField(default=True, blank=True, null=True)
    subdomain = models.BooleanField(default=True, blank=True, null=True)

    aaa = "BASIC (low budget)"

    def __str__(self):
        # return self.aaa
        return f" BASIC ${self.amount_doller} to {self.amonut_tk}tk"


class StanderdProduct(models.Model):
    amount_doller = models.CharField(max_length=100, blank=True, null=True)
    amonut_tk = models.CharField(max_length=100, blank=True, null=True)
    disk_space = models.BooleanField(default=True, help_text="50GB disk space", blank=True, null=True)
    email_account = models.BooleanField(default=True, help_text="50 Email Account", blank=True, null=True)
    bandwith = models.BooleanField(default=True, help_text="50GB disk spacet", blank=True, null=True)
    maintenance = models.BooleanField(default=True, blank=True, null=True)
    subdomain = models.BooleanField(default=True, blank=True, null=True)

    aaa = "STANDERD (mid budget)"

    def __str__(self):
        return f" STANDERED ${self.amount_doller} to {self.amonut_tk}tk"


class ProProduct(models.Model):
    amount_doller = models.CharField(max_length=100, blank=True, null=True)
    amonut_tk = models.CharField(max_length=100, blank=True, null=True)
    disk_space = models.BooleanField(default=True, help_text="50GB disk space", blank=True, null=True)
    email_account = models.BooleanField(default=True, help_text="50 Email Account", blank=True, null=True)
    bandwith = models.BooleanField(default=True, help_text="50GB disk spacet", blank=True, null=True)
    maintenance = models.BooleanField(default=True, blank=True, null=True)
    subdomain = models.BooleanField(default=True, blank=True, null=True)

    aaa = "PRO (high budget)"

    def __str__(self):
        return f" PRO ${self.amount_doller} to {self.amonut_tk}tk"


class Product(models.Model):
    product_name = models.CharField(max_length=222, blank=True, null=True)
    product_demo_link = models.URLField()
    basic = models.ForeignKey(BasicProduct, on_delete=models.CASCADE, blank=True, null=True)
    standerd = models.ForeignKey(StanderdProduct, on_delete=models.CASCADE, blank=True, null=True)
    pro = models.ForeignKey(ProProduct, on_delete=models.CASCADE, blank=True, null=True)


class OurWork(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField(default="Description")
    demo=models.URLField(blank=True,default="https://jstutul.xyz")
    image=models.ImageField(upload_to="Our Work/",default="ourwork.jpg")

    def __str__(self):
        return self.title


class WorkList(models.Model):
    work = models.ForeignKey(OurWork, on_delete=models.CASCADE, related_name='w_list')
    desc = models.CharField(max_length=214)
    short_desc = models.CharField(max_length=221)
    img = models.ImageField(upload_to='ourworks')


class TeamMember(models.Model):
    img = models.FileField(upload_to='teammember', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    describe = models.TextField(max_length=999, null=True, blank=True)
    facebook_link = models.URLField(max_length=999, null=True, blank=True)
    instagram_link = models.URLField(max_length=999, null=True, blank=True)
    whatsapp_link = models.URLField(max_length=999, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class AboutUs(models.Model):
    title1 = models.CharField(max_length=255, null=True, blank=True)
    field1 = models.TextField(max_length=999, null=True, blank=True)

    title2 = models.CharField(max_length=255, null=True, blank=True)
    field2 = models.TextField(max_length=999, null=True, blank=True)

    title3 = models.CharField(max_length=255, null=True, blank=True)
    field3 = models.TextField(max_length=999, null=True, blank=True)

    title4 = models.CharField(max_length=255, null=True, blank=True)
    field4 = models.TextField(max_length=999, null=True, blank=True)


class Items(models.Model):
    name = models.CharField(max_length=100, blank=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '{}-{}'.format(self.name, self.status)


class Package(models.Model):
    name = models.CharField(max_length=30, blank=False)
    price = models.FloatField(default=1000)
    demo = models.URLField(blank=True)
    items = models.ManyToManyField(to="Items", blank=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=100, blank=False)
    package = models.ManyToManyField(to="Package", blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_service = models.ForeignKey(Services, on_delete=models.DO_NOTHING)
    order_package = models.ForeignKey(Package, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    orderId = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(str(self.user))

    def get_payment_url(self):
        return reverse("payment", kwargs={"id": self.id})

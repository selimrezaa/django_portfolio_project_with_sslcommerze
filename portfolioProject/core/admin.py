from django.contrib import admin
from .models import AboutUs, ContactModel, Header, HomePageTitleAndExtra,HomePageTopSlider,HomePageYouGet,HomePageWeComplete, OurWorksSection,OurWorks,TeamMember, Footer
# Register your models here.




admin.site.register(ContactModel)
admin.site.register(HomePageYouGet)
admin.site.register(HomePageWeComplete)
admin.site.register(OurWorksSection)
admin.site.register(OurWorks)
admin.site.register(TeamMember)
admin.site.register(AboutUs)


class HeaderAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(Header, HeaderAdmin)


class HomePageTitleAndExtraAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(HomePageTitleAndExtra, HomePageTitleAndExtraAdmin)


class HomePageTopSliderAdmin(admin.ModelAdmin):
  list_display = ('img',)

admin.site.register(HomePageTopSlider, HomePageTopSliderAdmin)


class FooterAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(Footer, FooterAdmin)
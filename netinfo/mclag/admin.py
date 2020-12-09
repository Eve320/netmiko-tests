from django.contrib import admin
from .models import Host
from django.conf.urls import url
from django.contrib.admin import AdminSite
from django.http import HttpResponse, HttpRequest, JsonResponse

class MyAdminSite(AdminSite):

    def custom_view(self, request):
        return HttpResponse("Test")

    def get_urls(self):
        from django.conf.urls import url
        urls = super(MyAdminSite, self).get_urls()
        urls += [
            url(r'^my_view/$', self.admin_view(self.custom_view))
        ]
        return urls

admin_site = MyAdminSite()

# Register your models here.
@admin.register(Host, site=admin_site)
class SomeModelAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Host)
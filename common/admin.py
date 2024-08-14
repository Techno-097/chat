from django.contrib import admin
from common.models import Home
from common.models import Not
from common.models import Image
from common.models import Useful
from common.models import All

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title", "description")


@admin.register(Not)
class NotAdmin(admin.ModelAdmin):
    list_display = ("title", "text")




@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    lost_display = ("name", "position")



@admin.register(Useful)
class UsefulAdmin(admin.ModelAdmin):
    lost_display = ("about", "text", "name")


@admin.register(All)
class AllAdmin(admin.ModelAdmin):
    lost_display = ("image", "category")
# Register your models here.
